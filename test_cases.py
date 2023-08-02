import time
import HtmlTestRunner
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Config.config import Config
from PageObject.Pages.login import Login
from PageObject.Pages.home import HomePage


class PythonLogin(unittest.TestCase):

    def setUp(self):
        serv = Service(Config.CHROME_EXECUTABLE_PATH)
        opts = webdriver.ChromeOptions()
        # opts.add_argument("--headless")
        opts.add_argument("disable-infobars")
        opts.add_argument("--disable-extensions")
        opts.add_argument("--disable-popup-blocking")
        opts.add_argument('--profile-directory=Default')
        opts.add_argument('--disable-gpu')
        opts.add_argument('--no-sandbox')
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument('--log-level=3')
        self.driver = webdriver.Chrome(service=serv, options=opts)
        self.driver.maximize_window()  # Maximize the window
        self.driver.set_page_load_timeout(30)
        self.driver.get(Config.BASE_URL)  # Launch the url in chrome
        print(self.driver.title, self.driver.current_url)  # Show page title and current url

    def test_registration_login(self):
        driver = self.driver
        login = Login(driver)
        Login.click_create_account(login)
        Login.create_new_account(login, Config.FNAME, Config.LNAME,
                                 Config.EMAIL, Config.PASSWORD)

        home = HomePage(driver, True)
        HomePage.click_logout(home)

    def test_login_logout(self):
        driver = self.driver
        login = Login(driver, Config.VALID_USER, Config.VALID_PASSWORD)
        Login.click_sign_in_btn(login)

        home = HomePage(driver)
        HomePage.click_logout(home)

    def test_invalid_login(self):
        driver = self.driver
        login = Login(driver, Config.INVALID_USER, Config.INVALID_PASSWORD)
        Login.click_sign_in_btn(login)
        Login.is_invalid_user(login)

    def test_blank_login(self):
        driver = self.driver
        login = Login(driver)
        Login.set_blank_fields(login)
        Login.click_sign_in_btn(login)
        Login.is_invalid_user(login)

    def tearDown(self):
        if self.driver is not None:
            print("EXIT: Cleanup of test environment")
            # yield self.driver
            # self.driver.close()  # Close the current browser window
            self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=Config.REPORT_PATH))

