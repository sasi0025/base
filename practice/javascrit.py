import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")# we use execute script method to execute java scripts and for also scrolling purpose.
time.sleep(2)