from selenium import webdriver
from selenium.webdriver.common.by import By
bag=[]
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
elemnets=driver.find_elements(By.XPATH,"//tr/td[1]")

for i in elemnets:
    bag.append(i.text)
originalbag=bag
bag.sort()


assert originalbag== bag

