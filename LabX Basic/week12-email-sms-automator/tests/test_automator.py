# email-sms-automator/tests/test_automator.py
"""Unit tests ที่จำลอง SMTP/IMAP ด้วย unittest.mock (ไม่ต้องใช้อินเทอร์เน็ตหรือรหัสผ่านจริง)"""
import email
import imaplib
import logging
import os
import shutil
import smtplib
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from email_receiver import EmailReceiver  # noqa: E402
from email_sender import EmailSender  # noqa: E402
from sms_gateway import SMSGateway  # noqa: E402
from utils import ensure_directory_exists, get_env_variable, setup_logging  # noqa: E402

logging.disable(logging.CRITICAL)  # ไม่ให้ log รกผลการทดสอบ


class TestUtils(unittest.TestCase):
    def test_setup_logging_no_duplicate_handlers(self):
        a = setup_logging("dup_test")
        b = setup_logging("dup_test")
        self.assertIs(a, b)
        self.assertEqual(len(a.handlers), 1)

    def test_get_env_variable(self):
        with patch.dict(os.environ, {"MY_VAR": "value"}):
            self.assertEqual(get_env_variable("MY_VAR"), "value")
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                get_env_variable("MISSING_VAR")

    def test_ensure_directory_exists(self):
        tmp = tempfile.mkdtemp()
        target = os.path.join(tmp, "a", "b")
        ensure_directory_exists(target)
        self.assertTrue(os.path.isdir(target))
        shutil.rmtree(tmp)


class TestEmailSender(unittest.TestCase):
    def setUp(self):
        self.sender = EmailSender("smtp.test.com", 587, "me@test.com", "app-pass")
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    @patch("smtplib.SMTP")
    def test_connect_success_uses_starttls_and_login(self, mock_smtp_class):
        server = mock_smtp_class.return_value
        self.assertTrue(self.sender._connect())
        server.starttls.assert_called_once()
        server.login.assert_called_once_with("me@test.com", "app-pass")

    @patch("smtplib.SMTP")
    def test_connect_authentication_error(self, mock_smtp_class):
        mock_smtp_class.return_value.login.side_effect = smtplib.SMTPAuthenticationError(535, b"Auth failed")
        self.assertFalse(self.sender._connect())
        self.assertIsNone(self.sender.server)

    @patch("smtplib.SMTP", side_effect=smtplib.SMTPConnectError(421, "refused"))
    def test_connect_connection_error(self, _):
        self.assertFalse(self.sender._connect())

    @patch("smtplib.SMTP")
    def test_send_email_with_thai_subject_and_attachment(self, mock_smtp_class):
        path = os.path.join(self.tmp, "report.pdf")
        with open(path, "wb") as f:
            f.write(b"%PDF-1.4 test")
        self.assertTrue(self.sender.send_email("you@test.com", "ทดสอบ หัวข้อ", "สวัสดี", attachment_path=path))
        msg = mock_smtp_class.return_value.send_message.call_args[0][0]
        self.assertEqual(msg["To"], "you@test.com")
        self.assertEqual(msg["Subject"], "ทดสอบ หัวข้อ")
        self.assertEqual([a.get_filename() for a in msg.iter_attachments()], ["report.pdf"])
        mock_smtp_class.return_value.quit.assert_called_once()

    @patch("smtplib.SMTP")
    def test_send_email_missing_attachment_still_sends(self, mock_smtp_class):
        self.assertTrue(self.sender.send_email("you@test.com", "S", "B", attachment_path="nope.pdf"))
        msg = mock_smtp_class.return_value.send_message.call_args[0][0]
        self.assertEqual(list(msg.iter_attachments()), [])

    def test_dry_run_writes_eml(self):
        s = EmailSender("x", 1, "me@test.com", "", dry_run=True, outbox_dir=self.tmp)
        self.assertTrue(s.send_email("you@test.com", "Hello", "Body"))
        files = os.listdir(self.tmp)
        self.assertEqual(len(files), 1)
        self.assertTrue(files[0].endswith(".eml"))


class TestEmailReceiver(unittest.TestCase):
    def setUp(self):
        self.receiver = EmailReceiver("imap.test.com", "me@test.com", "app-pass")
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    @patch("imaplib.IMAP4_SSL")
    def test_connect_auth_failure(self, mock_imap_class):
        mock_imap_class.return_value.login.side_effect = imaplib.IMAP4.error("AUTHENTICATIONFAILED")
        self.assertFalse(self.receiver._connect())

    @patch("imaplib.IMAP4_SSL")
    def test_search_emails_quotes_arguments(self, mock_imap_class):
        imap = mock_imap_class.return_value
        imap.uid.return_value = ("OK", [b"5 7"])
        uids = self.receiver.search_emails(from_sender="me@test.com", subject_contains="Receiving Demo")
        self.assertEqual(uids, [b"5", b"7"])
        imap.uid.assert_called_with("search", None, "UNSEEN", "FROM", '"me@test.com"', "SUBJECT", '"Receiving Demo"')
        imap.logout.assert_called_once()

    def test_decode_header_part_thai(self):
        encoded = email.header.Header("ทดสอบ", "utf-8").encode()
        self.assertEqual(EmailReceiver._decode_header_part(encoded), "ทดสอบ")
        self.assertEqual(EmailReceiver._decode_header_part(None), "")

    @patch("imaplib.IMAP4_SSL")
    def test_fetch_email_content_downloads_and_marks_read(self, mock_imap_class):
        sender = EmailSender("x", 1, "me@test.com", "")
        pdf = os.path.join(self.tmp, "report.pdf")
        with open(pdf, "wb") as f:
            f.write(b"%PDF data")
        raw = bytes(sender.build_message("me@test.com", "ทดสอบ Demo", "x" * 300, attachment_path=pdf))
        imap = mock_imap_class.return_value
        imap.uid.side_effect = [("OK", [(b"5 (RFC822)", raw)]), ("OK", [b""])]
        out_dir = os.path.join(self.tmp, "attachments")
        details = self.receiver.fetch_email_content(b"5", download_attachments_dir=out_dir)
        self.assertEqual(details["subject"], "ทดสอบ Demo")
        self.assertEqual(details["sender"], "me@test.com")
        self.assertEqual(len(details["body_snippet"]), 200)
        self.assertEqual(details["attachments_downloaded"], ["report.pdf"])
        self.assertTrue(os.path.exists(os.path.join(out_dir, "report.pdf")))
        imap.uid.assert_called_with("store", b"5", "+FLAGS", "(\\Seen)")


class TestSMSGateway(unittest.TestCase):
    def setUp(self):
        self.sender = MagicMock(spec=EmailSender)
        self.sender.send_email.return_value = True
        self.sms = SMSGateway.__new__(SMSGateway)
        self.sms.email_sender = self.sender

    def test_requires_email_sender(self):
        with self.assertRaises(TypeError):
            SMSGateway("not a sender")

    def test_send_with_carrier(self):
        self.assertTrue(self.sms.send_sms("123-456-7890", "hi", "att"))
        self.sender.send_email.assert_called_once_with("1234567890@txt.att.net", subject="", body="hi")

    def test_send_to_direct_gateway_address_and_truncate(self):
        self.sms.send_sms("555@vtext.com", "a" * 200)
        _, kwargs = self.sender.send_email.call_args
        self.assertEqual(len(kwargs["body"]), 160)

    def test_unknown_carrier(self):
        self.assertFalse(self.sms.send_sms("1234567890", "hi", "ais"))
        self.sender.send_email.assert_not_called()


if __name__ == "__main__":
    unittest.main()
