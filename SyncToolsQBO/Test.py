import unittest
from selenium import webdriver
from html_testRunner import HTMLTestRunner  # Assuming HTMLTestRunner is available in the project

class TestExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="reports"))
