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
#GitHUb 
"""from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up headless Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run in headless mode
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
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

# Set up the WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")  # Uncomment if needed
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Positive Test Case: Valid Login
@allure.feature('Login Tests')
@allure.story('Positive Test Case')
@allure.severity(allure.severity_level.BLOCKER)
def test_valid_login():
    driver = setup_driver()
    try:
        with allure.step("Navigate to the Sign-in page"):
            driver.get("https://app.synctools.io/sign-in")

        with allure.step("Enter email and password"):
            email = "neha@satvasolutions.com"
            password = "Satva1213#"  # Don't log actual passwords in real tests

            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_field.send_keys(email)

            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "basic_password"))
            )
            password_field.send_keys(password)

            allure.attach(email, name="Entered Email", attachment_type=allure.attachment_type.TEXT)
            allure.attach(password, name="Entered Password", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Click the Sign-in button"):
            button = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Sign in')]"))
            )
            button.click()

        with allure.step("Verify successful login"):
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://app.synctools.io/")
            )
            assert driver.current_url == "https://app.synctools.io/"
            allure.attach(driver.current_url, name="Final URL", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Capture screenshot of dashboard"):
            allure.attach(driver.get_screenshot_as_png(), name="Dashboard Screenshot", attachment_type=allure.attachment_type.PNG)

    finally:
        driver.quit()

# Negative Test Case: Invalid Login (Wrong Password)
@allure.feature('Login Tests')
@allure.story('Negative Test Case')
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login():
    driver = setup_driver()
    try:
        with allure.step("Navigate to the Sign-in page"):
            driver.get("https://app.synctools.io/sign-in")

        with allure.step("Enter email and incorrect password"):
            email = "neha@satvasolutions.com"
            password = "wrongpassword"  

            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_field.send_keys(email)

            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "basic_password"))
            )
            password_field.send_keys(password)

            allure.attach(email, name="Entered Email", attachment_type=allure.attachment_type.TEXT)
            allure.attach(password, name="Entered Password", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Click the Sign-in button"):
            button = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Sign in')]"))
            )
            button.click()

        with allure.step("Verify login failure"):
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://app.synctools.io/sign-in")
            )
            assert driver.current_url == "https://app.synctools.io/sign-in"
            allure.attach(driver.current_url, name="Final URL After Failed Login", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Capture screenshot of error message"):
            allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)

    finally:
        driver.quit()

# Negative Test Case: Blank Email and Password
@allure.feature('Login Tests')
@allure.story('Negative Test Case - Blank Fields')
@allure.severity(allure.severity_level.NORMAL)
def test_blank_email_password():
    driver = setup_driver()
    try:
        with allure.step("Navigate to the Sign-in page"):
            driver.get("https://app.synctools.io/sign-in")

        with allure.step("Click the Sign-in button without entering any credentials"):
            button = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Sign in')]"))
            )
            button.click()

        with allure.step("Check for error messages"):
            email_error_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='basic_email_help']//div[@class='ant-form-item-explain-error']"))
            )
            assert email_error_message.is_displayed(), "Email error message is not displayed"

            password_error_message = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='ant-form-item-explain-error' and contains(text(), 'Please enter your password')]"))
            )
            assert password_error_message.is_displayed(), "Password error message is not displayed"

        with allure.step("Capture screenshot of error messages"):
            allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot - Blank Fields", attachment_type=allure.attachment_type.PNG)
 

    finally:
        driver.quit()


