# agentic-comm-automator/src/communication_agent.py
import datetime
import json
import os

from email_tasks import EmailTasks
from sms_tasks import SMSTasks
from template_renderer import TemplateRenderer
from utils import ensure_directory_exists, get_env_variable, log_audit_entry, setup_logging

logger = setup_logging(__name__)


class CommunicationAgent:
    """
    Agent ที่ทำงานสื่อสาร (Email / SMS / Inbox rules) ตามลำดับ task ใน config
    - self.context: ข้อมูลกลางที่ใช้เติม template และส่งต่อผลลัพธ์ระหว่าง task (output_context_key)
    - self.audit_log: บันทึกทุกการกระทำ/การตัดสินใจของ agent แล้วบันทึกเป็นไฟล์ JSON
    """

    def __init__(self, config, base_dir, dry_run=False):
        self.config = config
        self.base_dir = base_dir
        self.audit_log = []
        self.context = {}
        self.renderer = TemplateRenderer()
        self.start_time = datetime.datetime.now()

        sender_email = get_env_variable("SENDER_EMAIL", "agent@example.com" if dry_run else None)
        password = "" if dry_run else get_env_variable("SENDER_APP_PASSWORD")
        self.email_tasks = EmailTasks(
            smtp_server=os.getenv("SMTP_SERVER", "smtp.gmail.com"),
            smtp_port=int(os.getenv("SMTP_PORT", "587")),
            imap_server=os.getenv("IMAP_SERVER", "imap.gmail.com"),
            sender_email=sender_email,
            sender_password=password,
            dry_run=dry_run,
            outbox_dir=os.path.join(base_dir, "outbox"),
            mock_inbox_dir=os.path.join(base_dir, "mock_inbox"),
        )
        self.sms_tasks = SMSTasks(self.email_tasks)
        self.handlers = {
            "send_email": self._task_send_email,
            "send_sms": self._task_send_sms,
            "process_inbox": self._task_process_inbox,
        }

        # ค่าเริ่มต้นใน context (เทียบได้กับข้อมูลรายงานที่ agent สร้างไว้ก่อนหน้า)
        self.context.update({
            "sender_email": sender_email,
            "recipient_email": os.getenv("TEST_RECIPIENT_EMAIL") or sender_email,
            "sms_phone": os.getenv("TEST_SMS_PHONE_NUMBER", "1234567890"),
            "sms_carrier": os.getenv("TEST_SMS_CARRIER", "att"),
            "report_name": "DailySalesSummary",
            "report_date": datetime.date.today().isoformat(),
            "sales_figure": 12345.67,
            "total_customers": 500,
        })
        self.context.update(config.get("context", {}))
        logger.info("CommunicationAgent initialized with task handlers.")

    # ------------------------------------------------------------------ helpers
    def _render(self, template, extra=None):
        return self.renderer.render(template, {**self.context, **(extra or {})})

    def _path(self, relative):
        return os.path.normpath(os.path.join(self.base_dir, relative))

    # ------------------------------------------------------------------ tasks
    def _task_send_email(self, params):
        recipients = {k: [self._render(r) for r in v] for k, v in params["recipients"].items()}
        subject = self._render(params["subject_template"])
        body = self._render(params["body_template"])
        attachments = [self._path(self._render(a)) for a in params.get("attachments", [])]
        ok = self.email_tasks.send_email(recipients, subject, body, attachments, params.get("is_html", False))
        return ok, {"recipients": recipients, "subject": subject}

    def _task_send_sms(self, params):
        numbers = [self._render(p) for p in params["phone_numbers"]]
        message = self._render(params["message_template"])
        carrier = self._render(params.get("carrier_name", "")) or None
        ok = self.sms_tasks.send_sms(numbers, message, carrier)
        return ok, {"phone_numbers": numbers, "message": message}

    @staticmethod
    def _rule_matches(cond, info):
        """ทุกเงื่อนไขใน 'if' ต้องเป็นจริง (AND) - เปรียบเทียบข้อความแบบไม่สนตัวพิมพ์เล็ก/ใหญ่"""
        checks = {
            "from_contains": lambda v: v.lower() in info["sender"].lower(),
            "subject_contains": lambda v: v.lower() in info["subject"].lower(),
            "body_contains": lambda v: v.lower() in info["text_body"].lower(),
            "has_attachments": lambda v: v == info["has_attachments"],
        }
        return all(checks[key](value) for key, value in cond.items() if key in checks)

    def _task_process_inbox(self, params):
        criteria = params["search_criteria"]
        mailbox = params.get("mailbox", "INBOX")
        ids = self.email_tasks.search_emails(
            mailbox=mailbox,
            criteria=criteria.get("status", "UNSEEN"),
            from_sender=self._render(criteria["from_sender"]) if criteria.get("from_sender") else None,
            subject_contains=self._render(criteria["subject_contains"]) if criteria.get("subject_contains") else None,
        )
        # อีเมลตอบกลับอัตโนมัติ (เช่น "Re: ...") ไม่ต้องประมวลผลซ้ำ ป้องกันการตอบกลับวนลูป
        ignore_prefixes = [p.lower() for p in params.get("ignore_subject_prefixes", ["Re:"])]
        processed = []
        for email_id in ids:
            info = self.email_tasks.fetch_email(email_id, mailbox)
            if info is None:
                continue
            if any(info["subject"].lower().startswith(p) for p in ignore_prefixes):
                logger.info(f"Skipping auto-reply email '{info['subject']}'.")
                continue
            fields = {k: v for k, v in info.items() if not k.startswith("_")}
            log_audit_entry(self.audit_log, "INFO", f"Processing email '{info['subject']}' from {info['sender']}",
                            "process_inbox", {"attachments": info["attachment_names"]})
            actions = []
            for idx, rule in enumerate(params["rules"], 1):
                cond = {k: self._render(v) if isinstance(v, str) else v for k, v in rule.get("if", {}).items()}
                if not self._rule_matches(cond, info):
                    continue
                then = rule.get("then", {})
                planned = [a for a in ("download_attachments", "send_sms_alert", "reply_with_template", "mark_as_read")
                           if then.get(a)]
                log_audit_entry(self.audit_log, "INFO", f"Rule {idx} matched -> actions {planned}", "rule_engine")
                if then.get("download_attachments"):
                    folder = self._path(self._render(then.get("download_dir", "data/incoming_attachments")))
                    saved = self.email_tasks.download_attachments(info, folder, then.get("allowed_extensions"))
                    actions.append(f"downloaded {len(saved)} attachment(s)")
                if then.get("send_sms_alert"):
                    numbers = [self._render(p, fields) for p in then.get("alert_phone_numbers", [])]
                    msg = self._render(then.get("alert_message_template", "New email: {subject}"), fields)
                    carrier = self._render(then.get("alert_carrier", "{sms_carrier}"), fields)
                    if self.sms_tasks.send_sms(numbers, msg, carrier):
                        actions.append("sms alert sent")
                if then.get("reply_with_template"):
                    body = self._render(then["reply_with_template"], fields)
                    subject = self._render(then.get("reply_subject_template", "Re: {subject}"), fields)
                    if self.email_tasks.send_email({"to": [info["sender"]]}, subject, body):
                        actions.append("auto-reply sent")
                if then.get("mark_as_read"):
                    self.email_tasks.mark_as_read(email_id, mailbox)
                    actions.append("marked as read")
            processed.append({"subject": info["subject"], "actions": actions})
        return True, {"emails_found": len(ids), "processed": processed}

    # ------------------------------------------------------------------ run
    def _process_task(self, task):
        name, task_type = task["name"], task["type"]
        logger.info(f"Executing task: '{name}' (Type: {task_type})")
        log_audit_entry(self.audit_log, "INFO", f"Starting task '{name}'", task_type)
        try:
            ok, output = self.handlers[task_type](task.get("parameters", {}))
        except Exception as e:
            log_audit_entry(self.audit_log, "ERROR", f"Task '{name}' raised an error: {e}", task_type)
            logger.error(f"Error during task '{name}': {e}", exc_info=True)
            return False
        if ok and task.get("output_context_key"):
            self.context[task["output_context_key"]] = output
        log_audit_entry(self.audit_log, "SUCCESS" if ok else "ERROR",
                        f"Task '{name}' {'completed' if ok else 'failed'}.", task_type, output)
        return ok

    def _send_error_alert(self, failed):
        """แจ้งเตือนทางอีเมลเมื่อมี task ล้มเหลว (ถ้ากำหนด on_error_notify ใน config)"""
        target = self.config.get("on_error_notify")
        if not target or not failed:
            return
        body = "The Communication Agent finished with failed task(s):\n- " + "\n- ".join(failed)
        self.email_tasks.send_email({"to": [self._render(target)]}, "[Agent Alert] Task failure", body)

    def _save_audit_report(self):
        folder = self._path("reports")
        ensure_directory_exists(folder)
        path = os.path.join(folder, f"audit_report_comm_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.audit_log, f, indent=4, ensure_ascii=False)
        logger.info(f"Audit report saved to: {os.path.relpath(path, self.base_dir)}")

    def run(self):
        log_audit_entry(self.audit_log, "INFO", "Communication Agent started.", "agent_run",
                        {"dry_run": self.email_tasks.dry_run})
        failed = [t["name"] for t in self.config["tasks"] if not self._process_task(t)]
        duration = (datetime.datetime.now() - self.start_time).total_seconds()
        log_audit_entry(self.audit_log, "INFO",
                        f"Finished {len(self.config['tasks']) - len(failed)}/{len(self.config['tasks'])} "
                        f"task(s) successfully in {duration:.2f}s.", "agent_run_summary")
        self._send_error_alert(failed)
        self._save_audit_report()
        return not failed
