from selenium import webdriver
driver = webdriver.Chrome() # we can use whaterver browser same code applicable for all the browsers
driver.get("https://www.google.com/")# to go to the destiny url
driver.maximize_window() # to maximize the window
print(driver.title) # to get the tittle
print(driver.current_url) # to get the current url
driver.get("https://www.jio.com/")
driver.minimize_window() # to minimize the window
print(driver.title)
driver.back()
print(driver.current_url)
driver.refresh()