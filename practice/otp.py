import imaplib
from typing import re


class otp:
    def get_otp(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        email_username = 'sasikumar@neokred.tech'
        email_password = '9047317209@sasi'

        mail.login(email_username, email_password)
        mail.select('INBOX')

        _, message_ids = mail.search(None, 'SUBJECT "OTP Verification for Admin Login"')

        otp = None

        if message_ids and len(message_ids[0].split()) > 0:
            latest_message_id = message_ids[0].split()[-1]
            _, message_data = mail.fetch(latest_message_id, '(RFC822)')

            for response_part in message_data:
                if isinstance(response_part, tuple):
                    message_content = response_part[1].decode('utf-8')

                    otp_pattern = r'\b\d{6}\b'
                    match = re.search(otp_pattern, message_content)

                    if match:
                        otp = match.group()

        mail.logout()

        return otp