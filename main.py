import re
from imapclient import IMAPClient

def get_otp_from_mail(username, password):
    # Connect to the mail server (Gmail in this example)
    server = IMAPClient('imap.gmail.com', ssl=True)
    server.login(username, password)

    # Select the mailbox to search for OTP emails
    server.select_folder('INBOX')

    # Search for emails with the OTP keyword in the subject or body
    otp_search_criteria = ['SUBJECT "OTP"']
    messages = server.search(otp_search_criteria)

    otp = None

    # Retrieve the latest OTP email
    if messages:
        latest_message_id = messages[-1]
        response = server.fetch(latest_message_id, ['BODY[]'])
        message_body = response[latest_message_id][b'BODY[]'].decode('utf-8')

        # Extract the OTP from the email body using a regular expression
        otp_pattern = r'\b\d{6}\b'  # Assuming the OTP is a 6-digit number
        match = re.search(otp_pattern, message_body)

        if match:
            otp = match.group()

    # Disconnect from the mail server
    server.logout()

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
