from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"openwindow").click()
windowopen = driver.window_handles
driver.switch_to.window(windowopen[1])
print(driver.current_url)
# driver.find_element(By.XPATH,"//div[@class='header-contact text-lg-left text-center']//span[contains(text(),'info@qaclickacademy.com')]")
driver.switch_to.window(windowopen[0])
print(driver.current_url)