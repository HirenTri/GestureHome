from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# Path to your WebDriver (update with the actual path)
driver_path = "C:\Users\sagar\Downloads\ChromeSetup.exe"

# Set up the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the page
channel = 1
driver.get(f"http://127.0.0.1:5500/web_page/page{channel}.html")

# Wait for a few seconds (or perform actions)
time.sleep(5)

# Close the current tab
driver.close()

# If you're done with the browser entirely
driver.quit()
