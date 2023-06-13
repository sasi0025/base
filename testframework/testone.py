import time
from selenium.webdriver.support.expected_conditions import EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.autosuggestivedropdown import driver
from base.utilities.baseclass import baseclass

class testone(baseclass):

    def test_login(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
        products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            productname = product.find_element(By.XPATH, "div/h4").text
            if productname == 'Blackberry':
                product.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("india")
        self.wait = WebDriverWait(driver, 10)
        self. wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, "India"))
        self.driver.find_element(By.LINK_TEXT, "INDIA").click()
        self.driver.find_element(By.ID, "checkbox2").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        print(driver.find_element(By.CSS_SELECTOR, ".alert alert-success alert-dismissible").text)







