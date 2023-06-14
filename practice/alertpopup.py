import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#top")
driver.find_element(By.XPATH,"//input[@placeholder='Enter Your Name']").send_keys("sasi")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
pop=driver.switch_to.alert # we use switch to alert method to handle pop up because we can't handle them in html we can handle only in java
#time.sleep(2)
print(pop.text)
pop.accept() # it is used to accept
#pop.dismiss()# it is used to cancel


