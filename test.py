import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class BaseTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, username, password,OTP):
        self.driver.get("https://preprod-giverly-admin.neokredx.com/login")  # Replace with your login URL

        # Enter username and password
        self.driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(username)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(2)

        # Click on login button
        self.driver.find_element(By.XPATH, "//button[@data-testid='button']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys(OTP)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@data-testid='button']").click()
        time.sleep(2)
    #def logout(self):
        # Perform logout steps
        #self.driver.find_element(By.XPATH, "//button[text()='Logout']").click()  # Replace with your logout button locator

    def run_test(self):
        # Usage example
        self.login("sasikumar@neokred.tech", "Neokred@123")


ob=BaseTest()
ob.login("sasikumar@neokred.tech","Neokred@123","123456")

