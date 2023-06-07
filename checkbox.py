
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for check in checkbox:
    if check.get_attribute("value")== 'option2':
        check.click()
        print(check.is_enabled())
