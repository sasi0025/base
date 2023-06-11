import re
import imaplib

def get_otp_from_mail(username, password):

    mail = imaplib.IMAP4_SSL('imap.gmail.com')


    mail.login(username, password)


    mail.select('INBOX')


    _, message_ids = mail.search(None, 'SUBJECT "OTP"')

    otp = None


    if message_ids[0]:
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


email_username = 'sasikumar@neokred.tech'
email_password = '9047317209@sasi'

otp = get_otp_from_mail(email_username, email_password)

if otp:
    print("OTP found:", otp)
else:
    print("No OTP found in the mail.")
