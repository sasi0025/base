from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://preprod-giverly-client.neokredx.com/login")
driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys('sasikumar@neokred.tech')
driver.find_element(By.XPATH,"//input[@type='password']").send_keys('Neokred@123')
driver.find_element(By.XPATH,"//button[@data-testid='button']").click()
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("123456")
print(driver.current_url)

