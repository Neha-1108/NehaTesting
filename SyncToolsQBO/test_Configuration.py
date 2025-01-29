"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://app.synctools.io/sign-in")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# **Step 1: Login**
wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("neha@satvasolutions.com")
wait.until(EC.presence_of_element_located((By.ID, "basic_password"))).send_keys("Satva1213#")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in')]"))).click()

time.sleep(10)

# Waiting for the unique dashboard element to load
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-layout-sider-children']")))  # This confirms the dashboard is loaded


# **Step 3: Redirect to the Users Settings page**
driver.get("https://app.synctools.io/settings/shopify-x-qbo/Configuration")

time.sleep(10)

driver.quit()
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

# Load credentials from environment variables
email = os.getenv("SYNC_TOOLS_EMAIL")
password = os.getenv("SYNC_TOOLS_PASSWORD")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://app.synctools.io/sign-in")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# **Step 1: Login**
wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.ID, "basic_password"))).send_keys(password)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in')]"))).click()

# **Step 2: Wait for Dashboard**
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-layout-sider-children']")))

# **Step 3: Redirect to Configuration Page**
driver.get("https://app.synctools.io/settings/shopify-x-qbo/Configuration")

# **Step 4: Verify Page Loaded**
wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))  # Adjust as needed

# Close the driver
driver.quit()
