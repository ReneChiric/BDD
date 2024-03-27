from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# from BDD.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    EMAIL_INPUT = (By.CLASS_NAME, 'email')
    PASS_INPUT = (By.CLASS_NAME, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'login-button')
    ERROR_MSG_MAIN = (By.CSS_SELECTOR, 'div.message-error')
    ERROR_MSG_EMAIL = (By.ID, 'Email-error')
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Forgot password?']")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.type(self.PASS_INPUT, password)

    def click_login_btn(self):
        self.click(self.LOGIN_BUTTON)

    def click_forgot_password_link(self):
        self.click(self.FORGOT_PASSWORD_LINK)

    def is_main_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MSG_MAIN)

    def is_email_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MSG_EMAIL)

    def get_main_error_message_text(self):
        return self.get_element_text(self.ERROR_MSG_MAIN)

    def get_email_error_message_text(self):
        return self.get_element_text(self.ERROR_MSG_EMAIL)

    def set_unregistered_email(self):
        self.set_email("andsaj@host2.com")

    def set_wrong_password(self):
        self.set_password("2392094")

    def unregistered_account_message_displayed(self):
        return "No customer account found" in self.get_main_error_message_text()
