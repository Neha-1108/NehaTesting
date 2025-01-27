"""from selenium import webdriver
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
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up headless Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass sandbox for CI environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent issues related to shared memory in CI

# Set up WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open SyncTools login page
driver.get("https://app.synctools.io/sign-in")

# Wait for the email field to be present
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)
email_field.send_keys("neha@satvasolutions.com")

# Wait for the password field to be present
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "basic_password"))
)
password_field.send_keys("Satva1213#")  # Replace with actual password

# Wait for the sign-in button and click it
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Sign in']]"))
)
button.click()

# Wait for login to complete (you can adjust this if you need to check login success)


# Optionally, close the browser
driver.quit()

