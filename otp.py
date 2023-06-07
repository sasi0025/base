import imaplib
import email

def get_otp_from_email(username, password):
    # Connect to the email server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")  # Replace with your email server's IMAP address
    mail.login(username, password)

    # Select the inbox folder
    mail.select("inbox")

    # Search for emails containing OTP
    result, data = mail.search(None, 'SUBJECT "OTP"')  # Adjust the search criteria if needed

    otp = None

    if result == 'OK':
        email_ids = data[0].split()
        latest_email_id = email_ids[-1]  # Fetch the latest email

        # Retrieve the email
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]

        # Parse the email
        msg = email.message_from_bytes(raw_email)

        # Extract the OTP from the email body
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "TEXT":
                    otp = part.get_payload()
                    break
        else:
            otp = msg.get_payload()

    # Logout and close the connection
    mail.logout()



    return otp

# Example usage
username = "sasikumar@neokred.tech"  # Replace with your email address
password = "9047317209@sasi"  # Replace with your email password

otp = get_otp_from_email(username, password)

if otp:
    print("OTP:", otp)
else:
    print("No OTP found in the email.")
