import re
import imaplib

def get_otp_from_mail(username, password):
    # Connect to the mail server (Gmail in this example)
    mail = imaplib.IMAP4_SSL('imap.gmail.com')

    # Login to the mail server
    mail.login(username, password)

    # Select the mailbox to search for OTP emails
    mail.select('INBOX')

    # Search for emails with the subject containing "OTP"
    _, message_ids = mail.search(None, 'SUBJECT "OTP"')

    otp = None

    # Retrieve the latest OTP email
    if message_ids[0]:
        latest_message_id = message_ids[0].split()[-1]
        _, message_data = mail.fetch(latest_message_id, '(RFC822)')

        for response_part in message_data:
            if isinstance(response_part, tuple):
                message_content = response_part[1].decode('utf-8')

                # Extract the OTP from the email content using a regular expression
                otp_pattern = r'\b\d{6}\b'  # Assuming the OTP is a 6-digit number
                match = re.search(otp_pattern, message_content)

                if match:
                    otp = match.group()

    # Logout from the mail server
    mail.logout()

    return otp

# Provide your Gmail credentials
email_username = 'sasikumar@neokred.tech'
email_password = '9047317209@sasi'

# Retrieve the OTP from the mail
otp = get_otp_from_mail(email_username, email_password)

if otp:
    print("OTP found:", otp)
else:
    print("No OTP found in the mail.")
