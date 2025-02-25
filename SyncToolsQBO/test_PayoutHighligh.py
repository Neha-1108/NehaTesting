import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Helper function to highlight elements
def highlight_element(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)
    time.sleep(1)  # Highlight for 1 second before interacting

@allure.feature("Sales Orders and Shopify Payouts Navigation")
@allure.story("Click Sales Orders and Navigate to Shopify Payouts")
@allure.severity(allure.severity_level.CRITICAL)
def test_sales_orders_to_shopify_payouts():
    driver = setup_driver()
    
    try:
        with allure.step("Step 1: Navigate to the login page"):
            driver.get("https://app.synctools.io/sign-in")
            driver.maximize_window()

        with allure.step("Step 2: Enter login credentials and submit"):
            email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "basic_password"))
            )

            # Highlight the email and password input fields before entering
            highlight_element(driver, email)
            email.send_keys("neha@satvasolutions.com")
            
            highlight_element(driver, password)
            password.send_keys("Satva1213#")
            
            password.send_keys(Keys.RETURN)

            allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 3: Wait for dashboard to load"):
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Dashboard')]"))
            )

        with allure.step("Step 4: Click on Sales Orders"):
            sales_orders_card = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'Dashboard_sales-order-card')]//div[@class='ant-card-body']"))
            )

            # Highlight the Sales Orders element before clicking
            highlight_element(driver, sales_orders_card)
            sales_orders_card.click()

            allure.attach(driver.get_screenshot_as_png(), name="Sales Orders Clicked", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 5: Navigate to Shopify Payouts"):
            shopify_payouts = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Shopify Payouts"))
            )

            # Highlight the Shopify Payouts link before clicking
            highlight_element(driver, shopify_payouts)
            shopify_payouts.click()

            # Added a wait to make sure page has loaded before continuing
            time.sleep(2)

        with allure.step("Step 6: Verify Shopify Payouts page loaded"):
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://app.synctools.io/shopify-payouts")
            )

            # Added sleep for better visual observation if needed
            time.sleep(1)

            allure.attach(driver.get_screenshot_as_png(), name="Shopify Payouts Page", attachment_type=allure.attachment_type.PNG)

    finally:
        # Allow the page to settle before quitting the driver
        time.sleep(2)  # Adjust the sleep duration if needed for verification
        driver.quit()
