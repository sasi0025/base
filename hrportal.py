from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

from urllib3.util import current_time


# Function to login
def login(driver, username, password):
    driver.get("https://neokred.greythr.com/uas/portal/auth/login?login_challenge=6aebff2f49cc48cdb1ba486e24481e5a")  # Replace with your login URL
    username_input = driver.find_element(By.ID, "username")  # Replace with the actual username input element's ID
    password_input = driver.find_element(By.ID, "password")  # Replace with the actual password input element's ID
    login_button = driver.find_element(By.CSS_SELECTOR, ".mb-9.bg-primary.h-21.items-center.justify-center.text-white.flex.w-full.text-7gpx.font-body-semibold.rounded-gt-md-3")  # Replace with the actual login button element's CSS selector

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()


# Function to sign in at 9:30 AM
def sign_in(driver):
    current_time = datetime.now().strftime("%H:%M")
    if current_time == "09:30":
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn btn-primary btn-medium")))  # Replace with the actual sign-in button element's class name

        sign_in_button.click()


# Function to sign out at 6:30 PM
def sign_out(driver):
    current_time = datetime.now().strftime("%H:%M")
    if current_time == "18:30":
        sign_out_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn btn-primary btn-medium")))  # Replace with the actual sign-out button element's class name

        sign_out_button.click()


# Function to generate a report
def generate_report(event):
    with open("report.txt", "a") as report_file:  # Adjust the file path if needed
        current_time
