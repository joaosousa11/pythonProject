import time
from selenium.webdriver.common.action_chains import ActionChains
from PageObject.locators import Locator
from PageObject.Pages.base_page import BasePage


class Login(BasePage):

    def __init__(self, driver, user=None, password=None):
        super().__init__(driver)
        self.driver = driver

        self.credentials_card = driver.find_element(*Locator.credentials_card)
        self.user = driver.find_element(*Locator.user)
        self.password = driver.find_element(*Locator.password)
        self.sign_in = driver.find_element(*Locator.login_btn)
        self.create_account = driver.find_element(*Locator.new_account_btn)

        self.is_login_available()

        if user:
            self.set_user(user)
        if password:
            self.set_password(password)

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user.clear()
        self.user.send_keys(user)

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password.clear()
        self.password.send_keys(password)

    def login(self, user, password):
        self.set_user(user)
        self.set_password(password)

    # NEW ACCOUNT

    def get_firstname(self):
        return self.driver.find_element(*Locator.inp_fname)

    def set_firstname(self, fname):
        first = self.get_firstname()
        first.clear()
        first.send_keys(fname)
        assert fname == first.get_attribute('value').strip()

    def get_lastname(self):
        return self.driver.find_element(*Locator.inp_lname)

    def set_lastname(self, lname):
        last = self.get_lastname()
        last.clear()
        last.send_keys(lname)
        assert lname == last.get_attribute('value').strip()

    def get_email(self):
        return self.driver.find_element(*Locator.inp_email)

    def set_email(self, email):
        mail = self.get_email()
        mail.clear()
        mail.send_keys(email)
        assert email == mail.get_attribute('value').strip()

    def get_new_password(self):
        return self.driver.find_element(*Locator.inp_password)

    def set_new_password(self, npassword):
        passw = self.get_new_password()
        passw.clear()
        passw.send_keys(npassword)
        assert npassword == passw.get_attribute('value').strip()

    def get_terms(self):
        self.wait_element_located(*Locator.chk_terms)
        return self.driver.find_element(*Locator.chk_terms)

    def set_terms(self):
        terms = self.get_terms()
        if not terms.is_selected():
            terms.click()
        assert terms.is_selected()

    def get_button(self):
        return self.sign_in

    def click_sign_in_btn(self):
        self.wait_element_located(*Locator.login_btn)
        self.sign_in.click()

    def click_create_account(self):
        self.wait_element_located(*Locator.new_account_btn)
        self.create_account.click()

    def get_credentials_card(self):
        return self.credentials_card

    def get_invalid_login(self):
        return self.find_element(*Locator.invalid_login)

    def get_invalid_user(self):
        return self.find_element(*Locator.email_error)

    def get_invalid_password(self):
        return self.find_element(*Locator.password_error)

    def click_sign_up_btn(self):
        self.wait_element_clickable(*Locator.sign_up_btn)
        sign_up = self.find_element(*Locator.sign_up_btn)
        assert sign_up.is_enabled() is True
        sign_up.click()

    def is_login_available(self):
        self.wait_element_visibility(*Locator.credentials_card)
        assert self.credentials_card

        # check if button is enable
        self.wait_element_located(*Locator.login_btn)
        assert self.sign_in.is_enabled() is True

        # check if user and password are available
        self.user.is_displayed()
        self.password.is_displayed()

        # print("Login - All elements are present!")

    def is_invalid_user(self):
        self.wait_element_visibility(*Locator.invalid_login)
        invalid_login = self.get_invalid_login()
        invtext = invalid_login.text
        assert invtext == 'Invalid email or password.'
        print(invtext)

    def set_blank_fields(self):
        self.set_user("")
        user = self.get_invalid_user()
        utext = user.get_attribute('innerText').strip()
        assert utext == 'Please enter a valid email address'
        print(utext)

        self.set_password("")
        password = self.get_invalid_password()
        ptext = password.get_attribute('innerText').strip()
        assert ptext == 'This field cannot be blank'
        print(ptext)

    def create_new_account(self, first_name, last_name, email, password):
        self.wait_element_visibility(*Locator.create_account_card)

        self.set_firstname(first_name)
        self.set_lastname(last_name)
        self.set_email(email)
        self.set_new_password(password)
        self.set_terms()

        self.click_sign_up_btn()




