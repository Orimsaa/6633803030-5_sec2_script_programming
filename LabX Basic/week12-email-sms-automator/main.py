# email-sms-automator/main.py
"""
Automated communication workflow:
  Task 1 ส่งอีเมลข้อความธรรมดา
  Task 2 ส่งอีเมลพร้อมไฟล์แนบ
  Task 3 ส่ง SMS ผ่าน Email-to-SMS gateway
  Task 4 ส่งอีเมลหาตัวเองแล้วรับ/อ่านผ่าน IMAP + ดาวน์โหลดไฟล์แนบ

ใช้ `python main.py --dry-run` เพื่อทดสอบโดยไม่ต้องมีรหัสผ่าน (อีเมลถูกบันทึกเป็นไฟล์ .eml ใน outbox/)
"""
import argparse
import email
import glob
import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "src"))

from email_receiver import EmailReceiver
from email_sender import EmailSender
from sms_gateway import SMSGateway
from utils import ensure_directory_exists, get_env_variable, setup_logging

logger = setup_logging("main")

STUDENT = "อัษฎาวุธ เรือนแก้ว รหัสนักศึกษา 663380303-5"
RECEIVE_SUBJECT = "Python Test: Email for Receiving Demo"


def load_settings(dry_run):
    if dry_run:  # ค่าตัวอย่าง ไม่มีการเชื่อมต่อจริง
        return dict(sender="student@example.com", password="", smtp="smtp.gmail.com", port=587,
                    imap="imap.gmail.com", recipient="teacher@example.com", phone="1234567890", carrier="att")
    return dict(sender=get_env_variable("SENDER_EMAIL"), password=get_env_variable("SENDER_APP_PASSWORD"),
                smtp=get_env_variable("SMTP_SERVER"), port=int(get_env_variable("SMTP_PORT")),
                imap=get_env_variable("IMAP_SERVER"), recipient=get_env_variable("TEST_RECIPIENT_EMAIL"),
                phone=get_env_variable("TEST_SMS_PHONE_NUMBER"), carrier=get_env_variable("TEST_SMS_CARRIER"))


def show_details(details):
    logger.info(f"  Sender: {details['sender']}")
    logger.info(f"  Subject: {details['subject']}")
    logger.info(f"  Body Snippet: {details['body_snippet']}")
    if details["attachments_downloaded"]:
        logger.info(f"  Attachments downloaded: {', '.join(details['attachments_downloaded'])}")
    else:
        logger.info("  No attachments downloaded for this email.")


def main():
    parser = argparse.ArgumentParser(description="Email & SMS automator")
    parser.add_argument("--dry-run", action="store_true", help="save emails to outbox/ instead of sending")
    args = parser.parse_args()

    data_dir = os.path.join(BASE_DIR, "data")
    attachments_dir = os.path.join(data_dir, "attachments")
    outbox_dir = os.path.join(BASE_DIR, "outbox")
    ensure_directory_exists(attachments_dir)

    try:
        s = load_settings(args.dry_run)
    except ValueError as e:
        logger.critical(f"Configuration error: {e}. Copy .env.example to .env and fill in your values "
                        "(or run 'python main.py --dry-run').")
        sys.exit(1)

    delay = 0 if args.dry_run else 1
    sender = EmailSender(s["smtp"], s["port"], s["sender"], s["password"], dry_run=args.dry_run, outbox_dir=outbox_dir)
    receiver = EmailReceiver(s["imap"], s["sender"], s["password"])
    sms = SMSGateway(sender)
    report = os.path.join(data_dir, "dummy_report.pdf")

    logger.info("--- Task 1: Sending a simple plaintext email ---")
    sender.send_email(s["recipient"], "ทดสอบ Automated Python Test Email", STUDENT)
    time.sleep(2 * delay)

    logger.info("--- Task 2: Sending an email with an attachment ---")
    sender.send_email(s["recipient"], "ทดสอบ Python Test Email with Attachment - Daily Report",
                      f"{STUDENT}\nแนบรายงานประจำวัน (dummy_report.pdf)", attachment_path=report)
    time.sleep(2 * delay)

    logger.info("--- Task 3: Sending an SMS via email gateway ---")
    sms.send_sms(s["phone"], "ทดสอบ Hello from Python! This is an automated SMS via email gateway.", s["carrier"])
    time.sleep(5 * delay)

    logger.info("--- Task 4: Receiving and processing emails ---")
    sender.send_email(s["sender"], f"ทดสอบ {RECEIVE_SUBJECT}", STUDENT, attachment_path=report)
    if args.dry_run:
        # จำลองกล่องจดหมาย: อ่านอีเมลล่าสุดที่ส่งหาตัวเองจาก outbox
        latest = sorted(glob.glob(os.path.join(outbox_dir, "*.eml")))[-1]
        with open(latest, "rb") as f:
            logger.info(f"[DRY-RUN] Reading {os.path.basename(latest)} as the incoming email")
            show_details(EmailReceiver.parse_message(email.message_from_bytes(f.read()), attachments_dir))
    else:
        logger.info("Sent a demo email to self. Waiting 10 seconds for delivery...")
        time.sleep(10)
        uids = receiver.search_emails(criteria="UNSEEN", from_sender=s["sender"], subject_contains=RECEIVE_SUBJECT)
        if not uids:
            logger.info("No matching unread emails found for receiving demo.")
        for uid in uids:
            details = receiver.fetch_email_content(uid, mark_as_read=True, download_attachments_dir=attachments_dir)
            if details:
                logger.info(f"Processing email UID: {details['uid']}")
                show_details(details)

    logger.info("--- All communication automation tasks completed ---")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    main()
