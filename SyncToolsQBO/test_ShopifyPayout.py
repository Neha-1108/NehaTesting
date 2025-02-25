import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

@allure.feature("Shopify Payouts")
@allure.story("Navigate and Open Payout Details")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopify_payouts():
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

            email.send_keys("neha@satvasolutions.com")
            password.send_keys("Satva1213#")
            password.send_keys(Keys.RETURN)

            allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 3: Wait for dashboard and navigate to Shopify Payouts"):
            WebDriverWait(driver, 15).until(
                EC.url_to_be("https://app.synctools.io/")
            )

            shopify_payouts = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Shopify Payouts"))
            )
            shopify_payouts.click()

        with allure.step("Step 4: Wait for Shopify Payouts page to load and click first payout row"):
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://app.synctools.io/shopify-payouts")
            )

            first_payout = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//tr[contains(@class, 'ant-table-row')][1]//td[contains(@class, 'payout-row-not-display')]"))
            )
            first_payout.click()

            allure.attach(driver.get_screenshot_as_png(), name="Payout Details Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 5: Scroll through the payout details"):
            actions = ActionChains(driver)

            for _ in range(10):  # Adjust range as needed
                actions.scroll_by_amount(0, 500).perform()  # Scroll down by 500 pixels
                WebDriverWait(driver, 1)  # Small delay for smooth scrolling

            # Scroll to bottom using JavaScript
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    finally:
        driver.quit()
