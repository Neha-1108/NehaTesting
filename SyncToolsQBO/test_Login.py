from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Ensure you have chrome driver installed)
driver = webdriver.Chrome()

# Open SyncTools login page
driver.get("https://app.synctools.io/sign-in")

# Wait for the page to load
time.sleep(2)

# Enter email
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("neha@satvasolutions.com")

# Enter password
password_field = driver.find_element(By.ID, "basic_password")
password_field.send_keys("Satva1213#")  # Replace with actual password

# Click the sign-in button
button = driver.find_element(By.XPATH, "//button[span[text()='Sign in']]")
button.click()

# Wait for login to complete
time.sleep(5)

# Optionally, close the browser
driver.quit()
