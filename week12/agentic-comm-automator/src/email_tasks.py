# agentic-comm-automator/src/email_tasks.py
import email
import email.utils
import imaplib
import json
import mimetypes
import os
import re
import smtplib
from datetime import datetime
from email.header import decode_header
from email.message import EmailMessage

from utils import ensure_directory_exists, setup_logging

logger = setup_logging(__name__)


class EmailTasks:
    """
    ส่งอีเมล (SMTP) และอ่าน/จัดการอีเมลขาเข้า (IMAP)

    dry_run=True: ไม่เชื่อมต่อเซิร์ฟเวอร์จริง แต่บันทึกอีเมลเป็นไฟล์ .eml ใน outbox_dir
    และถ้าผู้รับเป็นตัวเอง (sender_email) จะ "ส่งถึง" mock inbox (โฟลเดอร์) ด้วย
    ทำให้ทดสอบ workflow ทั้งหมด (รวมถึง process_inbox) ได้โดยไม่ต้องมีรหัสผ่าน
    """

    def __init__(self, smtp_server, smtp_port, imap_server, sender_email, sender_password,
                 dry_run=False, outbox_dir="outbox", mock_inbox_dir="mock_inbox"):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.imap_server = imap_server
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.dry_run = dry_run
        self.outbox_dir = outbox_dir
        self.mock_inbox_dir = mock_inbox_dir
        self._counter = 0
        mode = "DRY-RUN (no real email is sent)" if dry_run else f"LIVE via {smtp_server}:{smtp_port}"
        logger.info(f"EmailTasks initialized for {sender_email} - {mode}.")

    # ------------------------------------------------------------------ sending
    def _build_message(self, recipients, subject, body, attachments=None, is_html=False):
        msg = EmailMessage()
        msg["From"] = self.sender_email
        msg["To"] = ", ".join(recipients.get("to", []))
        if recipients.get("cc"):
            msg["Cc"] = ", ".join(recipients["cc"])
        msg["Subject"] = subject
        msg["Date"] = email.utils.formatdate(localtime=True)
        if is_html:
            plain = re.sub(r"<[^>]+>", "", body)
            msg.set_content(plain)
            msg.add_alternative(body, subtype="html")
        else:
            msg.set_content(body)

        attached = []
        for path in attachments or []:
            if not os.path.exists(path):
                logger.warning(f"Attachment file not found: {path}. Skipping.")
                continue
            ctype, _ = mimetypes.guess_type(path)
            maintype, subtype = (ctype or "application/octet-stream").split("/", 1)
            with open(path, "rb") as f:
                msg.add_attachment(f.read(), maintype=maintype, subtype=subtype,
                                   filename=os.path.basename(path))
            attached.append(os.path.basename(path))
        return msg, attached

    def _save_eml(self, msg, folder, flags=None):
        ensure_directory_exists(folder)
        self._counter += 1
        name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{self._counter:02d}.eml"
        path = os.path.join(folder, name)
        with open(path, "wb") as f:
            f.write(bytes(msg))
        if flags is not None:
            self._write_flags(folder, name, flags)
        return path

    def send_email(self, recipients, subject, body, attachments=None, is_html=False):
        to_list = recipients.get("to", [])
        all_recipients = to_list + recipients.get("cc", []) + recipients.get("bcc", [])
        if not all_recipients:
            logger.error("No recipients specified for email.")
            return False
        msg, attached = self._build_message(recipients, subject, body, attachments, is_html)

        if self.dry_run:
            path = self._save_eml(msg, self.outbox_dir)
            if self.sender_email in all_recipients:
                self._save_eml(msg, self.mock_inbox_dir, flags={"seen": False})
            logger.info(f"[DRY-RUN] Email to {', '.join(to_list)} saved as {os.path.basename(path)}. "
                        f"Subject: '{subject}' | Attachments: {attached or 'none'}")
            return True

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                # BCC ไม่อยู่ใน header แต่ส่งถึงผ่าน to_addrs
                server.send_message(msg, from_addr=self.sender_email, to_addrs=all_recipients)
            logger.info(f"Email sent to {', '.join(to_list)}. Subject: '{subject}' | Attachments: {attached or 'none'}")
            return True
        except smtplib.SMTPAuthenticationError:
            logger.error("SMTP login failed. Check SENDER_EMAIL / SENDER_APP_PASSWORD (use a Gmail App Password).")
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
        return False

    # ------------------------------------------------------------------ mock inbox helpers
    def _flags_path(self, folder):
        return os.path.join(folder, "_flags.json")

    def _read_flags(self, folder):
        try:
            with open(self._flags_path(folder), encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _write_flags(self, folder, name, flags):
        data = self._read_flags(folder)
        data[name] = flags
        with open(self._flags_path(folder), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    # ------------------------------------------------------------------ receiving
    @staticmethod
    def _imap_quote(value):
        return '"' + value.replace('"', '') + '"'

    def search_emails(self, mailbox="INBOX", criteria="UNSEEN", from_sender=None, subject_contains=None):
        """คืนค่ารายการ id ของอีเมลที่ตรงเงื่อนไข"""
        if self.dry_run:
            flags = self._read_flags(self.mock_inbox_dir)
            ids = []
            for name in sorted(flags):
                if criteria == "UNSEEN" and flags[name].get("seen"):
                    continue
                with open(os.path.join(self.mock_inbox_dir, name), "rb") as f:
                    msg = email.message_from_bytes(f.read())
                if from_sender and from_sender.lower() not in self._decode(msg["From"]).lower():
                    continue
                if subject_contains and subject_contains.lower() not in self._decode(msg["Subject"]).lower():
                    continue
                ids.append(name)
            logger.info(f"[DRY-RUN] Found {len(ids)} email(s) in mock inbox matching criteria.")
            return ids

        try:
            with imaplib.IMAP4_SSL(self.imap_server) as imap:
                imap.login(self.sender_email, self.sender_password)
                imap.select(mailbox)
                query = [criteria]
                if from_sender:
                    query += ["FROM", self._imap_quote(from_sender)]
                if subject_contains:
                    query += ["SUBJECT", self._imap_quote(subject_contains)]
                status, data = imap.uid("search", None, *query)
                uids = [u.decode() for u in data[0].split()] if status == "OK" else []
                logger.info(f"Found {len(uids)} email(s) in '{mailbox}' matching {query}.")
                return uids
        except Exception as e:
            logger.error(f"Error searching emails: {e}")
            return []

    def fetch_email(self, email_id, mailbox="INBOX"):
        """ดึงอีเมล 1 ฉบับ (ยังไม่ mark as read) คืนค่า dict ข้อมูลที่ parse แล้ว + message ดิบ"""
        if self.dry_run:
            with open(os.path.join(self.mock_inbox_dir, email_id), "rb") as f:
                msg = email.message_from_bytes(f.read())
        else:
            try:
                with imaplib.IMAP4_SSL(self.imap_server) as imap:
                    imap.login(self.sender_email, self.sender_password)
                    imap.select(mailbox)
                    status, data = imap.uid("fetch", email_id, "(BODY.PEEK[])")
                    if status != "OK" or not data or data[0] is None:
                        return None
                    msg = email.message_from_bytes(data[0][1])
            except Exception as e:
                logger.error(f"Error fetching email {email_id}: {e}")
                return None

        body = ""
        attachments = []
        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            filename = part.get_filename()
            if filename:
                attachments.append(self._decode(filename))
            elif part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", errors="replace")
        return {
            "uid": email_id,
            "sender": email.utils.parseaddr(self._decode(msg["From"]))[1],
            "subject": self._decode(msg["Subject"]),
            "text_body": body.strip(),
            "has_attachments": bool(attachments),
            "attachment_names": attachments,
            "_message": msg,
        }

    def download_attachments(self, email_info, target_dir, allowed_extensions=None):
        """บันทึกไฟล์แนบลงโฟลเดอร์ (เลือกเฉพาะนามสกุลที่กำหนดได้)"""
        ensure_directory_exists(target_dir)
        saved = []
        for part in email_info["_message"].walk():
            filename = part.get_filename()
            if not filename:
                continue
            filename = os.path.basename(self._decode(filename))
            if allowed_extensions and os.path.splitext(filename)[1].lower() not in allowed_extensions:
                logger.info(f"Skipping attachment '{filename}' (extension not allowed).")
                continue
            path = os.path.join(target_dir, filename)
            with open(path, "wb") as f:
                f.write(part.get_payload(decode=True))
            saved.append(path)
            logger.info(f"Downloaded attachment: {path}")
        return saved

    def mark_as_read(self, email_id, mailbox="INBOX"):
        if self.dry_run:
            self._write_flags(self.mock_inbox_dir, email_id, {"seen": True})
            return True
        try:
            with imaplib.IMAP4_SSL(self.imap_server) as imap:
                imap.login(self.sender_email, self.sender_password)
                imap.select(mailbox)
                imap.uid("store", email_id, "+FLAGS", "(\\Seen)")
            return True
        except Exception as e:
            logger.error(f"Error marking email {email_id} as read: {e}")
            return False

    @staticmethod
    def _decode(value):
        if value is None:
            return ""
        parts = []
        for part, charset in decode_header(value):
            if isinstance(part, bytes):
                parts.append(part.decode(charset or "utf-8", errors="replace"))
            else:
                parts.append(part)
        return "".join(parts).strip()
