import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
action=ActionChains(driver)
# for mouce acction we use action class
action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()
driver.implicitly_wait(5)

