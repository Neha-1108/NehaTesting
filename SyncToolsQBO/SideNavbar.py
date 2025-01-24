"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
time.sleep(5)

shopify_payouts = driver.find_element(By.CLASS_NAME, "ant-menu-item")
shopify_payouts.click()

# Wait for login to complete
time.sleep(5)

# Optionally, close the browser
driver.quit()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://app.synctools.io/sign-in")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

# Enter email
driver.find_element(By.ID, "email").send_keys("neha@satvasolutions.com")

# Enter password
driver.find_element(By.ID, "basic_password").send_keys("Satva1213#")  # Replace with actual password

# Click the Sign-in button
driver.find_element(By.XPATH, "//button[span[text()='Sign in']]").click()

# Wait for the dashboard to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ant-menu-item")))

# Find the Shopify Payouts menu item by `data-menu-id`
shopify_payouts = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[contains(@data-menu-id, 'shopify-payouts')]"))
)

# Scroll into view and click
driver.execute_script("arguments[0].scrollIntoView();", shopify_payouts)
shopify_payouts.click()

# Optionally, wait for navigation to the Payouts page
WebDriverWait(driver, 10).until(EC.url_contains("shopify-payouts"))

print("✅ Successfully navigated to Shopify Payouts!")

# Close the browser
driver.quit()
