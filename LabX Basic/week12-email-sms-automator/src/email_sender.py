# email-sms-automator/src/email_sender.py
"""ส่งอีเมลผ่าน SMTP (STARTTLS) รองรับข้อความธรรมดา/HTML และไฟล์แนบ"""
import mimetypes
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage
from email.utils import formatdate

from utils import ensure_directory_exists, setup_logging

logger = setup_logging(__name__)


class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password, dry_run=False, outbox_dir="outbox"):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.dry_run = dry_run          # True = บันทึกเป็นไฟล์ .eml แทนการส่งจริง
        self.outbox_dir = outbox_dir
        self.server = None
        self.sent_count = 0

    def _connect(self):
        """เชื่อมต่อ SMTP + STARTTLS + login คืนค่า True เมื่อสำเร็จ"""
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30)
            self.server.starttls()
            self.server.login(self.sender_email, self.sender_password)
            logger.info("Successfully connected and logged into SMTP server.")
            return True
        except smtplib.SMTPAuthenticationError as e:
            logger.error(f"SMTP authentication failed. Check email and app password. Error: {e}")
        except (smtplib.SMTPConnectError, OSError) as e:
            logger.error(f"SMTP connection failed. Check server address and port. Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during SMTP connect/login: {e}")
        self.server = None
        return False

    def _disconnect(self):
        if self.server:
            try:
                self.server.quit()
                logger.info("Disconnected from SMTP server.")
            except Exception as e:
                logger.warning(f"Error during SMTP disconnection: {e}")
            finally:
                self.server = None

    def build_message(self, recipient_email, subject, body, attachment_path=None, is_html=False):
        """สร้าง EmailMessage (รองรับภาษาไทยใน subject/body อัตโนมัติด้วย UTF-8)"""
        msg = EmailMessage()
        msg["From"] = self.sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg["Date"] = formatdate(localtime=True)
        msg.set_content(body, subtype="html" if is_html else "plain")
        if attachment_path:
            if os.path.exists(attachment_path):
                ctype, _ = mimetypes.guess_type(attachment_path)
                maintype, subtype = (ctype or "application/octet-stream").split("/", 1)
                with open(attachment_path, "rb") as f:
                    msg.add_attachment(f.read(), maintype=maintype, subtype=subtype,
                                       filename=os.path.basename(attachment_path))
                logger.info(f"Attached file: {os.path.basename(attachment_path)}")
            else:
                logger.warning(f"Attachment not found: {attachment_path}. Sending without it.")
        return msg

    def send_email(self, recipient_email, subject, body, attachment_path=None, is_html=False):
        msg = self.build_message(recipient_email, subject, body, attachment_path, is_html)
        if self.dry_run:
            ensure_directory_exists(self.outbox_dir)
            self.sent_count += 1
            path = os.path.join(self.outbox_dir, f"{datetime.now():%Y%m%d_%H%M%S}_{self.sent_count:02d}.eml")
            with open(path, "wb") as f:
                f.write(bytes(msg))
            logger.info(f"[DRY-RUN] Email to {recipient_email} saved as {os.path.basename(path)} | Subject: '{subject}'")
            return True
        if not self._connect():
            return False
        try:
            self.server.send_message(msg)
            logger.info(f"Email sent successfully to {recipient_email} | Subject: '{subject}'")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient_email}: {e}")
            return False
        finally:
            self._disconnect()
