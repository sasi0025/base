from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobutton=driver.find_elements(By.XPATH,"//input[@type='radio']")
for button in radiobutton:
    if button.get_attribute("value")=="radio2":
        button.click()
        print(button.is_selected())