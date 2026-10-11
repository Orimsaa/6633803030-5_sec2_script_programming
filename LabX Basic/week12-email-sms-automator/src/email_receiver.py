# email-sms-automator/src/email_receiver.py
"""รับ/ค้นหา/อ่านอีเมลผ่าน IMAP (SSL) และดาวน์โหลดไฟล์แนบ"""
import email
import imaplib
import os
from email.header import decode_header

from utils import ensure_directory_exists, setup_logging

logger = setup_logging(__name__)


class EmailReceiver:
    def __init__(self, imap_server, sender_email, sender_password):
        self.imap_server = imap_server
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.mail = None

    def _connect(self):
        try:
            self.mail = imaplib.IMAP4_SSL(self.imap_server)
            self.mail.login(self.sender_email, self.sender_password)
            logger.info("Successfully connected and logged into IMAP server.")
            return True
        except imaplib.IMAP4.error as e:
            logger.error(f"IMAP authentication failed. Check email, app password and that IMAP is enabled. Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during IMAP connect/login: {e}")
        self.mail = None
        return False

    def _disconnect(self):
        if self.mail:
            try:
                self.mail.logout()
                logger.info("Disconnected from IMAP server.")
            except Exception as e:
                logger.warning(f"Error during IMAP disconnection: {e}")
            finally:
                self.mail = None

    @staticmethod
    def _quote(value):
        """IMAP ต้องครอบข้อความที่มีช่องว่างด้วยเครื่องหมายคำพูด"""
        return '"' + value.replace('"', '') + '"'

    def search_emails(self, mailbox="INBOX", criteria="UNSEEN", from_sender=None, subject_contains=None):
        """ค้นหาอีเมล คืนค่ารายการ UID (bytes)"""
        if not self._connect():
            return []
        try:
            self.mail.select(mailbox)
            query = [criteria]
            if from_sender:
                query += ["FROM", self._quote(from_sender)]
            if subject_contains:
                query += ["SUBJECT", self._quote(subject_contains)]
            status, data = self.mail.uid("search", None, *query)
            if status != "OK":
                logger.error(f"IMAP search failed. Status: {status}")
                return []
            uids = data[0].split()
            logger.info(f"Found {len(uids)} email(s) matching {query}.")
            return uids
        except Exception as e:
            logger.error(f"Error searching emails: {e}")
            return []
        finally:
            self._disconnect()

    def fetch_email_content(self, uid, mark_as_read=True, download_attachments_dir=None, mailbox="INBOX"):
        """อ่านอีเมล 1 ฉบับ: ผู้ส่ง, หัวข้อ, เนื้อหา 200 ตัวอักษรแรก, ดาวน์โหลดไฟล์แนบ"""
        if not self._connect():
            return None
        try:
            self.mail.select(mailbox)
            status, data = self.mail.uid("fetch", uid, "(RFC822)")
            if status != "OK" or not data or data[0] is None:
                logger.error(f"Could not fetch email UID {uid}.")
                return None
            details = self.parse_message(email.message_from_bytes(data[0][1]), download_attachments_dir)
            if mark_as_read:
                self.mail.uid("store", uid, "+FLAGS", "(\\Seen)")
            details["uid"] = uid.decode() if isinstance(uid, bytes) else str(uid)
            return details
        except Exception as e:
            logger.error(f"Error fetching/parsing email UID {uid}: {e}")
            return None
        finally:
            self._disconnect()

    @classmethod
    def parse_message(cls, msg, download_attachments_dir=None):
        """แยกข้อมูลจาก email.message: ผู้ส่ง, หัวข้อ, เนื้อหา 200 ตัวอักษรแรก และบันทึกไฟล์แนบ"""
        body, downloaded = "", []
        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            filename = part.get_filename()
            if filename:
                filename = os.path.basename(cls._decode_header_part(filename))
                if download_attachments_dir:
                    ensure_directory_exists(download_attachments_dir)
                    path = os.path.join(download_attachments_dir, filename)
                    with open(path, "wb") as f:
                        f.write(part.get_payload(decode=True))
                    downloaded.append(filename)
                    logger.info(f"Downloaded attachment: {path}")
            elif part.get_content_type() == "text/plain" and not body:
                body = part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", errors="replace")
        return {
            "sender": cls._decode_header_part(msg["From"]),
            "subject": cls._decode_header_part(msg["Subject"]),
            "body_snippet": body.strip()[:200],
            "attachments_downloaded": downloaded,
        }

    @staticmethod
    def _decode_header_part(header_value):
        """ถอดรหัส MIME header (RFC 2047) เช่น =?utf-8?b?...?= ให้เป็นข้อความภาษาไทยปกติ"""
        if header_value is None:
            return ""
        parts = []
        for part, charset in decode_header(header_value):
            if isinstance(part, bytes):
                try:
                    parts.append(part.decode(charset or "utf-8"))
                except (LookupError, UnicodeDecodeError):
                    parts.append(part.decode("latin-1", errors="replace"))
            else:
                parts.append(part)
        return "".join(parts).strip()
