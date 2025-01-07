from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically download and use the ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver without additional options
driver = webdriver.Chrome(service=service)

# Replace with your email and password
email = "neha@satvasolutions.com"
password = "Satva1213#"

try:
    # Open the SyncTools login page
    driver.get("https://system.synctools.io/")

    # Wait for the page to load
    time.sleep(2)

    # Locate the email input field and enter the email
    email_field = driver.find_element(By.ID, "UserName")  # Using the 'id' attribute for the email field
    email_field.clear()
    email_field.send_keys(email)

    # Locate the password input field and enter the password
    password_field = driver.find_element(By.ID, "Password")  # Using the 'id' attribute for the password field
    password_field.clear()
    password_field.send_keys(password)

    # Locate the login button and click it
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")  # Locate using the 'input[type='submit']' selector
    login_button.click()

    # Wait to see if login is successful
    time.sleep(5)

    # You can now add further steps to verify successful login
    print("Login process attempted.")

finally:
    # Close the browser
    driver.quit()
