from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://corporate.baink.club/")
print(driver.title)
print(driver.current_url)
driver.close()