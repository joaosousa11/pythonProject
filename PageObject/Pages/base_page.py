from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from Config.config import Config


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_and_clear_input(self, *locator):
        temp = self.find_element_clickable(*locator)
        temp.send_keys(Keys.CONTROL, 'a')
        temp.send_keys(Keys.DELETE)
        return temp

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_element_clickable(self, *locator):
        self.wait_element_clickable(*locator)
        temp = self.driver.find_element(*locator)
        assert temp
        return temp

    def open(self, url):
        url = Config.BASE_URL + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # ELEMENTS .........................................................................................................

    def _element_click(self, *locator):
        self.wait_element_visibility(locator)
        self.find_element(*locator).click()

    def _element_send_keys(self, *locator, text):
        self.wait_element_visibility(locator)
        self.find_element(*locator).send_keys(text)

    def _element_get_text(self, *locator):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return elem.text

    def _element_is_visible(self, *locator):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(elem)

    def _get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    # WAITS ............................................................................................................

    def wait_element_located(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_all_elements_located(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_element_visibility(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_all_elements_visibility(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_element_invisibility(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()

    def wait_element_clickable(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
