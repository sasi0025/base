
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.getotp import otp


class WebBrowserAutomation(otp):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def close_browser(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.implicitly_wait(5)
        self.driver.get("https://preprod-giverly-client.neokredx.com/login")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys(username)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[@data-testid='button']").click()
        otp = self.get_otp()
        self.driver.find_element(By.XPATH,"//input[@type='password']").send_keys(otp)
        self.driver.find_element(By.XPATH,"//button[@data-testid='button']").click()






    def register(self, username, password, email):
        self.driver.get("https://example.com/register")
        username_input = self.driver.find_element_by_id("username")
        password_input = self.driver.find_element_by_id("password")
        email_input = self.driver.find_element_by_id("email")

        username_input.send_keys(username)
        password_input.send_keys(password)
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)

        # Wait for the registration process to complete
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

    def add_employee(self, employee_data):
        self.driver.get("https://example.com/dashboard")
        # Find the relevant elements and perform actions to add an employee

    def send_to_employee(self, employee_id, message):
        self.driver.get(f"https://example.com/employees/{employee_id}")
        # Find the relevant elements and perform actions to send a message to the employee

# Usage example:

get=WebBrowserAutomation()
get.login("sasij4565@gmail.com","Neokred@123")

# automation.add_employee(employee_data)
# automation.send_to_employee(employee_id, message)
# automation.close_browser()
