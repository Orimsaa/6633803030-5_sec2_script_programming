# agentic-comm-automator/src/sms_tasks.py
from email_tasks import EmailTasks
from utils import setup_logging

logger = setup_logging(__name__)


class SMSTasks:
    """
    ส่ง SMS ผ่าน Email-to-SMS gateway ของผู้ให้บริการเครือข่าย (เช่น 1234567890@txt.att.net)
    หมายเหตุ: ผู้ให้บริการในไทยส่วนใหญ่ไม่มี gateway แบบนี้ ในการใช้งานจริงควรใช้ API อย่าง Twilio
    """

    CARRIER_GATEWAYS = {
        "att": "@txt.att.net", "verizon": "@vtext.com", "tmobile": "@tmomail.net",
        "sprint": "@messaging.sprintpcs.com", "boost": "@sms.boostmobile.com",
    }

    def __init__(self, email_tasks_instance):
        if not isinstance(email_tasks_instance, EmailTasks):
            raise TypeError("SMSTasks requires an instance of EmailTasks.")
        self.email_tasks = email_tasks_instance
        logger.info("SMSTasks initialized.")

    def _gateway_address(self, phone_number, carrier_name=None):
        if "@" in phone_number:
            return phone_number
        if carrier_name and carrier_name.lower() in self.CARRIER_GATEWAYS:
            digits = "".join(ch for ch in phone_number if ch.isdigit())
            return digits + self.CARRIER_GATEWAYS[carrier_name.lower()]
        return None

    def send_sms(self, phone_numbers, message, carrier_name=None):
        """ส่งข้อความถึงทุกหมายเลข คืนค่า True เมื่อส่งสำเร็จครบทุกหมายเลข"""
        if not phone_numbers:
            logger.warning("No phone numbers provided for SMS.")
            return False
        sent = 0
        for number in phone_numbers:
            address = self._gateway_address(number, carrier_name)
            if not address:
                logger.warning(f"Unknown carrier for {number}. Cannot build SMS gateway address.")
                continue
            # SMS gateway ส่วนใหญ่จำกัด ~160 ตัวอักษร
            text = message if len(message) <= 160 else message[:157] + "..."
            logger.info(f"Sending SMS to {number} via gateway {address}")
            if self.email_tasks.send_email({"to": [address]}, subject="", body=text):
                sent += 1
        return sent == len(phone_numbers)
