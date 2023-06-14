from selenium.webdriver.common.by import By


class loginpage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@placeholder='Email']")
    password = (By.XPATH, "//input[@placeholder='Password']")
    login_button =(By.XPATH, "//button[@data-testid='button']")
    otp_field = (By.XPATH, "//input[@data-testid='input']")

    def username(self):
        return self.driver.find_element(*loginpage.username)
    def password(self):
        return self.driver.find_element(*loginpage.password)
    def login_button(self):
        return self.driver.find_element(*loginpage.login_button)
    def otp_field(self):
        return self.driver.find_element(*loginpage.otp_field)
