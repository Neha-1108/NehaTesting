from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Replace with the WebDriver of your choice
driver.maximize_window()

# Open the registration page
driver.get("https://system.synctools.io/Account/Register")  # Replace with the actual URL

try: 
    driver.find_element(By.ID, "UserName").send_keys("neha+1@satvasolutions.com")
    time.sleep(1)
    driver.find_element(By.ID, "FirstName").send_keys("Neha")
    time.sleep(1)
    driver.find_element(By.ID, "LastName").send_keys("Sharma")
    time.sleep(1)
    driver.find_element(By.ID, "CompanyName").send_keys("Test Company")
    time.sleep(1)
    driver.find_element(By.ID, "ContactNo").send_keys("1214567890")
    time.sleep(1)
    driver.find_element(By.ID, "Street").send_keys("121 Test Street")
    time.sleep(1)
    driver.find_element(By.ID, "City").send_keys("Ahmedabad")
    time.sleep(1)
    driver.find_element(By.ID, "State").send_keys("Gujarat")
    time.sleep(1)
    driver.find_element(By.ID, "Country").send_keys("India")
    time.sleep(1)
    driver.find_element(By.ID, "ZipCode").send_keys("180015")
    time.sleep(1)

    # Enter and confirm password
    driver.find_element(By.ID, "Password").send_keys("Test@1214")
    time.sleep(1)
    driver.find_element(By.ID, "ConfirmPassword").send_keys("Test@1214")
    time.sleep(1)

    # Select an integration from the dropdown
    wait = WebDriverWait(driver, 2) #2 Second wait for element to appear
    select_element = wait.until(EC.presence_of_element_located((By.ID, "ConnectionIntegration")))
    
    # Wait for 10 seconds before interacting with the dropdown
    time.sleep(10)

    # Create Select object
    select_integration = Select(select_element)

    # Select 'Linnworks to Xero' by visible text
    select_integration.select_by_visible_text("Linnworks to Xero")

    # Wait for the selection to be reflected in the UI
    time.sleep(3)

    # Submit the form
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Register']"))).click()
    
    # Wait to observe the result
    time.sleep(1)

    # Check for success (customize the condition based on the success message or URL)
    if "success" in driver.current_url.lower():
        print("Registration completed successfully!")
    else:
        print("Registration may have failed. Check the form or logs.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()