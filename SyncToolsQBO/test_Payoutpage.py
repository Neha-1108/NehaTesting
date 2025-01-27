from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Ensure you have chrome driver installed)
driver = webdriver.Chrome()

# Open SyncTools login page
driver.get("https://app.synctools.io/shopify-payouts")

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
# Open SyncTools login page
driver.get("https://app.synctools.io/shopify-payouts")
# Find the "Pending" element by its class name (or another unique identifier)
pending_element = driver.find_element(By.XPATH, "//span[contains(text(),'Pending')]")

# Click the "Pending" element
pending_element.click()

# Wait for the new page to load
time.sleep(3)  # Adjust the sleep time based on how long the new page takes to load

# Optionally, print the current URL to confirm the page opened
print(f"New page URL: {driver.current_url}")

# Close the browser after the task
driver.quit()
