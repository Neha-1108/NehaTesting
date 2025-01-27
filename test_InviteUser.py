from selenium import webdriver
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
time.sleep(2)

# Waiting for the unique dashboard element to load
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-layout-sider-children']")))  # This confirms the dashboard is loaded

# **Step 3: Redirect to the Users Settings page**
driver.get("https://app.synctools.io/settings/Users")
time.sleep(10)

# Wait for the "Invite User" button to be clickable, then click it to open the modal
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-lg']"))).click()
time.sleep(2)
wait.until(EC.presence_of_element_located((By.ID, "basic_name"))).send_keys("Neha Sharma")
time.sleep(2)
wait.until(EC.presence_of_element_located((By.ID, "basic_emailAddress"))).send_keys("neha@gmail.com")
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()

time.sleep(10)

driver.quit()