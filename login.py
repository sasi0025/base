import time
import re
import imaplib
from selenium import webdriver
from selenium.webdriver.common.by import By

class BaseTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        self.driver.get("https://giverly-admin.neokredx.com/login")


        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)



        self.driver.find_element(By.XPATH, "//button[@data-testid='button']").click()

        time.sleep(10)


        otp = self.get_otp()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//input[@data-testid='input']").send_keys(otp)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-testid='button']").click()
        time.sleep(2)

    def run_test(self):
        # Usage example
        self.login("sasikumar@neokred.tech", "Neokred@123",)

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
    def clint(self,):

        self.driver.find_element(By.XPATH,"//p[text()='client list']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"(//button[@data-testid='button'])[1]").click()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Company name']").send_keys("GIVERLY INDIA PRIVATE LIMITED")



ob = BaseTest()
ob.run_test()
oc=BaseTest()
oc.clint()

