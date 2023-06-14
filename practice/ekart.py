import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
assert  len(results)>1
for result in results:
    result.find_element(By.XPATH,"div/button").click()
driver.implicitly_wait(5) # it will wait upto 5 minutes if it it got element in 2 sec it will con tinue also or else it will wait till 5 sec
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
prices=driver.find_elements(By.XPATH,"//td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)
totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
if sum == totalamount:
    print("verified amount")
else:
    print("price variess")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
info=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
discountamount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
discountpercentage=(driver.find_element(By.CSS_SELECTOR,".discountPerc").text)
#assert  discountamount < totalamount
if discountamount < totalamount :
    print ("discount applied for the promo code is :  "+ discountpercentage)
else:
    print("no promo code applied")

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(2)
country=driver.find_elements(By.XPATH,"//div[@class='wrapperTwo']//div//select")
for c in country:
    if c.get_attribute("value") == 'Albania':
     c.click()

print(c.text)
driver.find_element(By.XPATH,"//input[@class='chkAgree']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']").click()
driver.get_screenshot_as_file("ekart.png")
driver.implicitly_wait()


