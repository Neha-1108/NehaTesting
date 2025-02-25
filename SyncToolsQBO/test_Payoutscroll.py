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

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="D:\AutomationTesting\chromedriver-win64\chromedriver.exe", options=chrome_options)
# Set up WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Helper function to apply pointer cursor style to all elements
def apply_pointer_cursor(driver, element):
    # Ensure the element is visible
    WebDriverWait(driver, 10).until(EC.visibility_of(element))

    # Apply pointer cursor style using JavaScript to the element
    driver.execute_script("arguments[0].style.cursor = 'pointer';", element)

    # Hover action (to simulate mouse movement)
    action = ActionChains(driver)
    action.move_to_element(element).perform()  # Hover
    time.sleep(1)  # Allow the pointer to be visible for a second
    
# Force Scroll function
def force_scroll_to_bottom(driver):
    print("Starting forced scrolling...")

    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(1)

    print("Scrolling using JavaScript...")
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });")
    time.sleep(2)

    print("Scrolling using Keyboard (PAGE_DOWN)...")
    body = driver.find_element(By.TAG_NAME, "body")
    for _ in range(10):  
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

    print("Scrolling using Mouse Wheel...")
    actions = ActionChains(driver)
    for _ in range(10):  
        actions.scroll_by_amount(0, 300).perform()
        time.sleep(0.5)

    print("Final attempt to scroll to absolute bottom...")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    allure.attach(driver.get_screenshot_as_png(), name="Final Scroll", attachment_type=allure.attachment_type.PNG)

@allure.feature("Sales Orders and Shopify Payouts Navigation")
@allure.story("Click Sales Orders and Navigate to Shopify Payouts")
@allure.severity(allure.severity_level.CRITICAL)
def test_sales_orders_to_shopify_payouts():
    driver = setup_driver()

    try:
        with allure.step("Step 1: Navigate to the login page"):
            driver.get("https://app.synctools.io/sign-in")
            driver.maximize_window()
            time.sleep(2)  # Delay to confirm page load

        with allure.step("Step 2: Enter login credentials and submit"):
            email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
            password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "basic_password")))

            email.send_keys("neha@satvasolutions.com")
            password.send_keys("Satva1213#")
            time.sleep(2)  # Delay before login submit

            password.send_keys(Keys.RETURN)  # Submit the form
            time.sleep(2)  # Delay to confirm login action

            allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 3: Wait for dashboard to load"):
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Dashboard')]")))
            time.sleep(2)  # Delay to confirm dashboard load

        with allure.step("Step 4: Click on Sales Orders"):
            sales_orders_card = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'Dashboard_sales-order-card')]//div[@class='ant-card-body']")))
            sales_orders_card.click()
            time.sleep(2)  # Delay to confirm click

            allure.attach(driver.get_screenshot_as_png(), name="Sales Orders Clicked", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 5: Navigate to Shopify Payouts"):
            shopify_payouts = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopify Payouts")))
            shopify_payouts.click()
            time.sleep(2)  # Delay to confirm navigation

        with allure.step("Step 6: Click on First Payout"):
            first_payout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//tr[contains(@class, 'ant-table-row')][1]//td[contains(@class, 'payout-row-not-display')]")))
            first_payout.click()
            time.sleep(2)  # Delay to confirm payout click

            allure.attach(driver.get_screenshot_as_png(), name="Payout Details Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 7: Scroll from top to bottom of the page"):
            force_scroll_to_bottom(driver)

    finally:
        time.sleep(2)  # Allow time for final screen checks before quitting
        driver.quit()
