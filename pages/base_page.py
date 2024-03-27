from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser





class BasePage(Browser):

    base_Url = "https://demo.nopcommerce.com/"



    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(expected_conditions.presence_of_element_located(element_locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def is_url_correct(self, expected_url):
        return expected_url == self.driver.current_url





