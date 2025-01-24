from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()

try:
    # Open SyncTools login page
    driver.get("https://app.synctools.io/sign-in")
    driver.maximize_window()
    
    wait = WebDriverWait(driver, 10)  # Explicit wait

    # Enter email
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys("neha@satvasolutions.com")

    # Enter password
    password_field = wait.until(EC.presence_of_element_located((By.ID, "basic_password")))
    password_field.send_keys("Satva1213#")  # Replace with actual password

    # Click the sign-in button
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in')]")))
    sign_in_button.click()

    # Wait for dashboard to load
    wait.until(EC.url_contains("/dashboard"))

    wait = WebDriverWait(driver, 10)
    sidebar = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ProjectLayout_layout__sidebar')]")))

# Click on the first div inside sidebar if needed
    first_item = sidebar.find_element(By.XPATH, "./div/div/div[1]")
    first_item.click()

    # Click on "Settings"
    settings_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div/div[@class='ant-popover css-1x4kt9h css-1x4kt9h ant-popover-placement-rightBottom']/div[@class='ant-popover-content']/div[@role='tooltip']/div[@class='ant-popover-inner-content']/div[@class='min-width-240px']/div/div[1]")))
    settings_option.click()

    # Click on "Configuration"
    config_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Configuration')]")))
    config_option.click()

    # Wait for page to load
    wait.until(EC.url_contains("/settings/shopify-x-qbo/Configuration"))

    # Scroll down
    driver.execute_script("window.scrollBy(0, 500);")

    # Select Frequency as "Daily"
    frequency_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@title='Daily']")))
    frequency_option.click()

    # Select Date - 01 Jan 2025
    date_picker = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select date']")))
    date_picker.clear()
    date_picker.send_keys("01/01/2025")

    # Click Save Button
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Save']")))
    save_button.click()

    # Wait for confirmation message (if any)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Successfully saved')]")))  # Adjust message if different

finally:
    # Close the browser
    driver.quit()
