import pytest
import allure
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Set up WebDriver with webdriver-manager
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return driver

@allure.feature("Store Switcher Dropdown & Navigation")
@allure.story("Login, Switch Store, Navigate to Shopify Payouts, Post to Xero, and Handle Failed Status")
@allure.severity(allure.severity_level.CRITICAL)
def test_switch_store():
    driver = setup_driver()
    
    try:
        with allure.step("Step 1: Navigate to the login page"):
            driver.get("https://app.synctools.io/sign-in")
            driver.maximize_window()
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "email")))
            time.sleep(2)

        with allure.step("Step 2: Enter login credentials and submit"):
            email = driver.find_element(By.ID, "email")
            password = driver.find_element(By.ID, "basic_password")

            email.send_keys("neha@satvasolutions.com")
            password.send_keys("Satva1213#")
            time.sleep(1)

            password.send_keys(Keys.RETURN)
            time.sleep(3)

            allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 3: Wait for dashboard to load"):
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Dashboard')]")))
            time.sleep(3)

        with allure.step("Step 4: Click on the Store Switcher Dropdown (techolab-uk)"):
            store_dropdown = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'techolab-uk')]"))
            )
            store_dropdown.click()
            time.sleep(4)

            allure.attach(driver.get_screenshot_as_png(), name="Dropdown Clicked", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 5: Select the new store 'techdemo-nz'"):
            new_store_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'techdemo-nz')]"))
            )
            new_store_option.click()
            time.sleep(3)

            allure.attach(driver.get_screenshot_as_png(), name="Store Switched", attachment_type=allure.attachment_type.PNG)

        with allure.step("Step 6: Navigate to Shopify Payouts"):
            shopify_payouts = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopify Payouts")))
            shopify_payouts.click()
            time.sleep(2)

        with allure.step("Step 7: Click on First Payout"):
            first_payout = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//tr[contains(@class, 'ant-table-row')][1]//td[contains(@class, 'payout-row-not-display')]"))
            )
            first_payout.click()
            time.sleep(2)

            allure.attach(driver.get_screenshot_as_png(), name="First Payout Clicked", attachment_type=allure.attachment_type.PNG)

        # Step 8: Click on "Post to Xero"
        with allure.step("Step 8: Click on 'Post to Xero'"):
            post_to_xero_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Post to Xero']"))
            )
            post_to_xero_button.click()
            print("✅ Clicked on 'Post to Xero'.")
            allure.attach(driver.get_screenshot_as_png(), name="Post to Xero Clicked", attachment_type=allure.attachment_type.PNG)

        # Step 9: Wait up to 5 minutes for "Pending" or "Failed" status
        with allure.step("Step 9: Wait for status update (up to 5 minutes)"):
            status_xpath = "//span[contains(@class, 'ml-2')]//span"
            start_time = time.time()
            timeout = 300  # 5 minutes (300 seconds)

            while time.time() - start_time < timeout:
                try:
                    current_status = driver.find_element(By.XPATH, status_xpath).text.strip()
                    print(f"🔄 Current Status: {current_status}")

                    if current_status == "Failed":
                        print("❌ Status changed to 'Failed'. Closing browser.")
                        allure.attach(driver.get_screenshot_as_png(), name="Status Failed", attachment_type=allure.attachment_type.PNG)
                        driver.quit()
                        return  # Exit test early

                    if current_status == "Pending":
                        print("✅ Status updated to 'Pending'. Proceeding.")
                        allure.attach(driver.get_screenshot_as_png(), name="Pending Status Confirmed", attachment_type=allure.attachment_type.PNG)
                        break  # Exit loop since "Pending" appeared

                except:
                    pass  # Continue waiting if status is not found yet

                time.sleep(10)  # Wait 10 seconds before checking again

            else:
                print("⚠ Timeout: Status did not update to 'Pending' or 'Failed' within 5 minutes.")
                allure.attach(driver.get_screenshot_as_png(), name="Status Timeout", attachment_type=allure.attachment_type.PNG)

    except (TimeoutException, NoSuchElementException) as e:
        allure.attach(driver.get_screenshot_as_png(), name="Exception Screenshot", attachment_type=allure.attachment_type.PNG)
        print(f"Exception occurred: {str(e)}")
        print(traceback.format_exc())

    finally:
        time.sleep(3)
        driver.quit()
