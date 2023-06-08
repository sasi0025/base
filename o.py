import imaplib
import email
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_otp_from_email(username, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("INBOX")
    result, data = mail.search(None, 'FROM "noreply@giverly.co" SUBJECT "OTP Verification for Admin Login"')

    otp = None
    if result == "OK":
        email_ids = data[0].split()
        latest_email_id = email_ids[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                otp = part.get_payload()
                break

    mail.logout()
    return otp


driver = webdriver.Chrome()
driver.get("https://giverly-admin.neokredx.com/login")


email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("sasikumar@neokred.tech")
password_input = driver.find_element(By.XPATH ,"//input[@placeholder='Password']").send_keys("Neokred@123")
login_button = driver.find_element(By.XPATH, "//button[@data-testid='button']").click()
time.sleep(10)

otp = fetch_otp_from_email("sasikumar@neokred.tech", "9047317209@sasi")
if otp is not None:

    otp_input = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH,"//input[@type='password']"))).send_keys(otp)

    verify_button = driver.find_element(By.XPATH,"//button[@data-testid='button']").click()


driver.implicitly_wait(5)
driver.quit()
