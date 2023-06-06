from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("sasi")
driver.find_element(By.NAME,"email").send_keys("sasij4565@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("sasi@1234")
driver.find_element(By.ID,"exampleCheck1").click()

