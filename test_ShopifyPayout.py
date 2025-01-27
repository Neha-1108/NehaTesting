from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver (Make sure you have chrome driver installed)
driver = webdriver.Chrome()

# Initialize ActionChains
actions = ActionChains(driver)

# Step 1: Open the login page
driver.get("https://app.synctools.io/login")  # Replace with the actual login URL
driver.maximize_window()

# Step 2: Log in (Modify as per your login fields)
username = driver.find_element(By.ID, "email")  # Replace with the actual name of the email field
password = driver.find_element(By.ID, "basic_password")  # Replace with the actual name of the password field

username.send_keys("neha@satvasolutions.com")  # Replace with actual email
password.send_keys("Satva1213#")  # Replace with actual password
password.send_keys(Keys.RETURN)  # Press Enter to submit login

time.sleep(5)  # Wait for the dashboard to load

# Step 3: Click on "Shopify Payouts" from the sidebar
shopify_payouts = driver.find_element(By.LINK_TEXT, "Shopify Payouts")  # Adjust locator if needed
shopify_payouts.click()

time.sleep(3)  # Wait for the page to load

# Step 4: # Click on the first payout row using the date column
first_payout = driver.find_element(By.XPATH, "//tr[contains(@class, 'ant-table-row')][1]//td[contains(@class, 'payout-row-not-display')]")
first_payout.click()

time.sleep(3)  # Wait for user to see the content

# Scroll down iteratively
for _ in range(10):  # Adjust range based on page height
    actions.scroll_by_amount(0, 500).perform()  # Scroll down by 500 pixels
    time.sleep(1)  # Small delay for smooth scrolling

# Alternatively, scroll to the bottom using JavaScript after using Actions
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


time.sleep(3)  # Wait for user to see the content

# Close the browser
driver.quit()
