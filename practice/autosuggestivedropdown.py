import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@placeholder='Type to Select Countries']").send_keys('ind')
time.sleep(2)
on=driver.find_elements(By.CSS_SELECTOR,"ul[class='ui-menu ui-widget ui-widget-content ui-autocomplete ui-front'] div")
print(len(on))
for i in on: # here we runnig loof to search the deseved word if the loop finds  the txt it will click
    if i.text=='India':
        i.click()
        break

assert driver.find_element(By.XPATH,"//input[@placeholder='Type to Select Countries']").get_attribute("value")=="India"
# when we the value is preloaded then to extract the value we use text() method
# if the value added by us dynamically then we need to use the get attribute () method and need to pass the value


