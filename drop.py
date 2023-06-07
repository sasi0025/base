import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.makemytrip.com/flights/?gclid=CjwKCAjw1YCkBhAOEiwA5aN4AWIFhxmctvdc5k9xt8WaR80fUfDVBy030uLEVTenHn7U013M10LP-hoCZPIQAvD_BwE&cmp=SEM|D|DF|G|Generic|DF_Generic_Exact|Flight_Exact|ETA|Regular|529647807040&s_kwcid=AL!1631!3!529647807040!e!!g!!flightbooking&ef_id=CjwKCAjw1YCkBhAOEiwA5aN4AWIFhxmctvdc5k9xt8WaR80fUfDVBy030uLEVTenHn7U013M10LP-hoCZPIQAvD_BwE:G:s")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@placeholder='From']")
fl=driver.find_elements(By.CSS_SELECTOR,"ul[class='react-autosuggest__suggestions-list'] li")
for i in fl:
    if i.text=='chennai':
        i.click()