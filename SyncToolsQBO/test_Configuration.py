#import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Test function for Login and redirect to Configuration page
def test_configuration_login():
    # Forcing the download and installation of the correct ChromeDriver
    chromedriver_path = ChromeDriverManager().install()
    print(f"ChromeDriver installed at: {chromedriver_path}")

# Create a Service object with the chromedriver path
    service = Service(chromedriver_path)
    # Initialize the WebDriver with the Service object
    driver = webdriver.Chrome(service=service)

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

# If you'd like to run the test directly, you can use:
if __name__ == "__main__":
    pytest.main()


"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Load credentials from environment variables
email = os.getenv("SYNC_TOOLS_EMAIL")
password = os.getenv("SYNC_TOOLS_PASSWORD")

# Check if environment variables are None
if email is None or password is None:
    raise ValueError("SYNC_TOOLS_EMAIL or SYNC_TOOLS_PASSWORD environment variables are not set.")

# Configure Chrome options to avoid session conflicts and improve stability
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9223")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")  # Remove this line for debugging
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")

# Initialize the WebDriver with the ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def test_configuration_login():
    try:
        # Step 1: Navigate to the sign-in page
        print("Navigating to sign-in page...")
        driver.get("https://app.synctools.io/sign-in")
        print("Navigated to the sign-in page.")

        # Log current URL to debug
        print("Current URL:", driver.current_url)

        # Wait for email input and login
        wait = WebDriverWait(driver, 30)  # Increased timeout to 30 seconds

        # Wait for email field to be visible and send keys
        print("Waiting for email field to be visible...")
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)
        print("Email entered")

        # Wait for password field and send keys
        print("Waiting for password field...")
        wait.until(EC.visibility_of_element_located((By.ID, "basic_password"))).send_keys(password)
        print("Password entered")

        # Wait for the sign-in button to be clickable and click it
        print("Waiting for Sign In button to be clickable...")
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in')]")))
        sign_in_button.click()
        print("Clicked Sign In button")

        # Step 2: Wait for the dashboard or any confirmation
        print("Waiting for dashboard to load...")
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-layout-sider-children']")))  # Change this according to actual UI

        # Step 3: Redirect to Configuration Page
        print("Navigating to Configuration Page...")
        driver.get("https://app.synctools.io/settings/shopify-x-qbo/Configuration")
        print("Navigated to Configuration Page")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
    # Additional logging if needed
        driver.save_screenshot('error_screenshot.png')  # Save screenshot for debugging
    finally:
        # Wait a little before quitting the driver to observe the state
        time.sleep(5)
        driver.quit()
        print("Driver closed")

# Call the function directly to check if the test works
test_configuration_login()

"""
"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Manually add credentials (email and password)
email = "neha@satvasolutions.com"
password = "Satva1213#"

# Configure Chrome options to avoid session conflicts and improve stability
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9223")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")  # Remove this line for debugging
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-extensions")

# Initialize the WebDriver with the ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def test_configuration_login():
    try:
        # Step 1: Navigate to the sign-in page
        print("Navigating to sign-in page...")
        driver.get("https://app.synctools.io/sign-in")
        print("Navigated to the sign-in page.")

        # Log current URL to debug
        print("Current URL:", driver.current_url)

        # Wait for email input and login
        wait = WebDriverWait(driver, 30)  # Increased timeout to 30 seconds

        # Wait for email field to be visible and send keys
        print("Waiting for email field to be visible...")
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)
        print("Email entered")

        # Wait for password field and send keys
        print("Waiting for password field...")
        wait.until(EC.visibility_of_element_located((By.ID, "basic_password"))).send_keys(password)
        print("Password entered")

        # Wait for the sign-in button to be clickable and click it
        print("Waiting for Sign In button to be clickable...")
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in')]")))
        sign_in_button.click()
        print("Clicked Sign In button")

        # Step 2: Wait for the dashboard or any confirmation
        print("Waiting for dashboard to load...")
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ant-layout-sider-children']")))  # Change this according to actual UI

        # Step 3: Redirect to Configuration Page
        print("Navigating to Configuration Page...")
        driver.get("https://app.synctools.io/settings/shopify-x-qbo/Configuration")
        print("Navigated to Configuration Page")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        # Additional logging if needed
        driver.save_screenshot('error_screenshot.png')  # Save screenshot for debugging
    finally:
        # Wait a little before quitting the driver to observe the state
        time.sleep(5)
        driver.quit()
        print("Driver closed")

# Call the function directly to check if the test works
test_configuration_login()
"""
