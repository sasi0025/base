
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Edge()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("sasi")
driver.find_element(By.NAME,"email").send_keys("sasij4565@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("sasi@1234")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
drop=Select(driver.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']"))# we use thie select method for drop downs
drop.select_by_visible_text('Male')
driver.find_element(By.XPATH,"//input[@type='submit' ]").click()

#if the dropdon is static then we use Select class to automate the dropdowns




