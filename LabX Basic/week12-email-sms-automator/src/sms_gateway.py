# email-sms-automator/src/sms_gateway.py
"""ส่ง SMS ผ่าน Email-to-SMS gateway ของผู้ให้บริการเครือข่าย (สหรัฐฯ)"""
from email_sender import EmailSender
from utils import setup_logging

logger = setup_logging(__name__)


class SMSGateway:
    CARRIER_GATEWAYS = {
        "att": "txt.att.net",
        "verizon": "vtext.com",
        "tmobile": "tmomail.net",
        "sprint": "messaging.sprintpcs.com",
        "boost": "sms.myboostmobile.com",
        "cricket": "sms.cricketwireless.net",
        "us_cellular": "email.uscc.net",
    }

    def __init__(self, email_sender_instance):
        if not isinstance(email_sender_instance, EmailSender):
            raise TypeError("SMSGateway requires an EmailSender instance.")
        self.email_sender = email_sender_instance

    def send_sms(self, phone_number, message, carrier_name=None):
        """
        phone_number: เบอร์ 10 หลัก (ใช้ร่วมกับ carrier_name) หรือที่อยู่ gateway เต็ม เช่น 1234567890@txt.att.net
        """
        if "@" in phone_number:
            address = phone_number
        elif carrier_name and carrier_name.lower() in self.CARRIER_GATEWAYS:
            digits = "".join(ch for ch in phone_number if ch.isdigit())
            address = f"{digits}@{self.CARRIER_GATEWAYS[carrier_name.lower()]}"
        else:
            logger.error(f"Unknown carrier '{carrier_name}' for {phone_number}. "
                         f"Supported: {', '.join(self.CARRIER_GATEWAYS)}")
            return False
        logger.info(f"Sending SMS to {phone_number} via gateway {address}")
        # gateway ส่วนใหญ่จำกัด 160 ตัวอักษร และแสดง subject รวมกับข้อความ จึงเว้น subject ว่าง
        return self.email_sender.send_email(address, subject="", body=message[:160])
