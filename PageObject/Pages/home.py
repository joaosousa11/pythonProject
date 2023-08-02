import time

from PageObject.locators import Locator
from PageObject.Pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver, new_user=False):
        super().__init__(driver)
        self.driver = driver

        self.is_home_available(new_user)

        if not new_user:
            self.get_sign_in_message()

        self.dashboard_title = driver.find_element(*Locator.my_dash_title)
        self.user_btn = driver.find_element(*Locator.user_dropdown)

    def is_home_available(self, new_user):
        # if not new_user:
        #     self.wait_element_visibility(*Locator.sign_in_message)

        self.wait_element_visibility(*Locator.my_dash_title)
        self.wait_element_clickable(*Locator.user_dropdown)

    def get_sign_in_message(self):
        self.wait_element_located(*Locator.sign_in_message)
        sign_in = self.find_element(*Locator.sign_in_message)
        assert sign_in.text == "Signed in successfully."
        print(sign_in.text)

    def click_logout_btn(self):
        # find and click 'logout' button
        self.wait_element_clickable(*Locator.user_dropdown)
        assert self.user_btn
        self.user_btn.click()

        self.wait_element_clickable(*Locator.log_out_opt)
        logout_opt = self.find_element(*Locator.log_out_opt)
        assert logout_opt
        logout_opt.click()

    def click_logout(self):
        # check home page
        self.is_home_available(False)
        assert self.dashboard_title

        self.click_logout_btn()

        self.wait_element_visibility(*Locator.main_page)
        print("Logout successfully.")

