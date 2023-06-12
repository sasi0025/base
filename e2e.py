import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[normalize-space()='Shop']").click()
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    productname =product.find_element(By.XPATH,"div/h4").text
    if productname == 'Blackberry':
        product.find_element(By.XPATH,"//button[@class='btn btn-info']").click()

time.sleep(3)
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.implicitly_wait(4)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("india")
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,"India"))
driver.find_element(By.LINK_TEXT,"INDIA").click()
driver.find_element(By.ID,"checkbox2").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
print(driver.find_element(By.CSS_SELECTOR,".alert alert-success alert-dismissible").text)
