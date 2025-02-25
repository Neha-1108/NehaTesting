import pytest
import allure
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  
    chrome_options.add_argument("--disable-popup-blocking")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

@allure.feature("Dropdown Selection Debugging")
@allure.story("Ensure 'Daily' is selected properly")
@allure.severity(allure.severity_level.CRITICAL)
def test_switch_store():
    driver = setup_driver()
    
    try:
        with allure.step("Step 1: Navigate to login page"):
            driver.get("https://app.synctools.io/sign-in")

        with allure.step("Step 2: Login with valid credentials"):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("neha@satvasolutions.com")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "basic_password"))).send_keys("Satva1213#" + Keys.RETURN)

        with allure.step("Step 3: Wait for Dashboard to load"):
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Dashboard')]")))

        with allure.step("Step 4: Open Settings"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Neha Sharma']"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Settings')]"))).click()

        with allure.step("Step 5: Click on Store Switcher Dropdown"):
            dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'ant-select-selector')]")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
            driver.execute_script("arguments[0].click();", dropdown)  # Force click
            
        with allure.step("Step 6: Wait for Dropdown to Open & Search for 'Daily'"):
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'ant-select-dropdown')]")))

            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'ant-select-search__field')]"))
            )
            search_box.send_keys("Daily")
            search_box.send_keys(Keys.ARROW_DOWN)  # Move down
            search_box.send_keys(Keys.ENTER)  # Select

        with allure.step("Step 7: Click Outside to Close Dropdown (if Needed)"):
            driver.find_element(By.TAG_NAME, "body").click()

        with allure.step("Step 8: Verify Selection"):
            selected_value = driver.find_element(By.XPATH, "//div[contains(@class,'ant-select-selection-item')]").text
            assert selected_value == "Daily", f"Expected 'Daily', but got '{selected_value}'"

        allure.attach(driver.get_screenshot_as_png(), name="Dropdown_Selected", attachment_type=allure.attachment_type.PNG)

    except (TimeoutException, NoSuchElementException) as e:
        allure.attach(driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        print(f"Exception: {str(e)}")
        print(traceback.format_exc())

    finally:
        driver.quit()
