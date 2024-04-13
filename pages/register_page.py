from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):

    MALE_RADIO_INPUT = (By.ID, "gender-male")
    FEMALE_RADIO_INPUT = (By.ID, "gender-female")
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    EMAIL_INPUT = (By.ID, "Email")
    COMPANY = (By.ID, "Company")
    PASSWORD_INPUT = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    YEAR_DROPDOWN = (By.NAME, "DateOfBirthYear")
    MONTH_DROPDOWN = (By.NAME, "DateOfBirthMonth")
    DAY_DROPDOWN = (By.NAME, "DateOfBirthDay")
    NEWSLETTER_CHECKBOX = (By.ID, "Newsletter")
    ALREADY_REGISTERED_EMAIL_ERROR = (By.CSS_SELECTOR, "div.message-error.validation-summary-errors")
    FIRST_PART_OF_THE_PASSWORD_ERROR = (By.XPATH, '//*[@id="Password-error"]/p')
    SECOND_PART_OF_THE_PASSWORD_ERROR = (By.XPATH, '//*[@id="Password-error"]/ul/li')


    ERROR_FIRST_NAME = (By.ID, 'FirstName-error')
    ERROR_LAST_NAME = (By.ID, 'LastName-error')
    EMAIL_ERROR = (By.ID, 'Email-error')
    PASSWORD_ERROR = (By.ID, 'Password-error')
    CONFIRM_PASSWORD_ERROR = (By.ID, 'ConfirmPassword-error')
    SUCCES_REGISTER_MESSAGE = (By.CLASS_NAME, 'result')

    REGISTER_PAGE_URL = "https://demo.nopcommerce.com/register"

    def navigate_to_register_page(self):
        self.driver.get(self.REGISTER_PAGE_URL)


    def select_day_dropdown(self, day):
        self.select_dropdown_option_by_text(self.DAY_DROPDOWN, day)

    def select_month_dropdown(self, month):
        self.select_dropdown_option_by_text(self.MONTH_DROPDOWN, month)

    def select_year_dropdown(self, year):
        self.select_dropdown_option_by_text(self.YEAR_DROPDOWN, year)

    def select_male_radio_button(self):
        self.click(self.MALE_RADIO_INPUT)

    def select_female_radio_button(self):
        self.click(self.FEMALE_RADIO_INPUT)

    def set_first_name(self, first_name):
        self.type(self.FIRST_NAME_INPUT, first_name)

    def set_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def click_on_register_button(self):
        self.click(self.REGISTER_BUTTON)

    def verify_first_name_error_displayed(self):
        assert self.is_element_displayed(self.ERROR_FIRST_NAME), "Mesajul nu este afisat"

    def verify_last_name_error_displayed(self):
        assert self.is_element_displayed(self.ERROR_LAST_NAME), "Mesajul nu este afisat"

    def verify_email_error_displayed(self):
        assert self.is_element_displayed(self.EMAIL_ERROR), "Mesajul nu este afisat"

    def verify_password_error_displayed(self):
        assert self.is_element_displayed(self.PASSWORD_ERROR), "Mesajul nu este afisat"

    def verify_confirm_password_error_displayed(self):
        assert self.is_element_displayed(self.CONFIRM_PASSWORD_ERROR), "Mesajul nu este afisat"


    def verify_succes_message_displayed(self):
        assert self.is_element_displayed(self.SUCCES_REGISTER_MESSAGE), "Mesajul de eroare nu este afisat"


    def get_succes_message_text(self):
        return self.get_element_text(self.SUCCES_REGISTER_MESSAGE)


    def get_password_error_message_text(self):
        return self.get_element_text(self.PASSWORD_ERROR)


    def get_password_confirmation_error_message_text(self):
        return self.get_element_text(self.CONFIRM_PASSWORD_ERROR)


    def get_email_error_message_text(self):
        return self.get_element_text(self.EMAIL_ERROR)


    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def set_confirm_password(self, password):
        self.type(self.CONFIRM_PASSWORD, password)


    def get_already_registered_email_error_text(self):
        return self.get_element_text(self.ALREADY_REGISTERED_EMAIL_ERROR)

    def verify_already_registered_email_error_displayed(self):
        assert self.is_element_displayed(self.ALREADY_REGISTERED_EMAIL_ERROR), "Mesajul nu este afisat"


    def verify_already_registered_email_error_text(self, expected_message):
        actual_message = self.get_already_registered_email_error_text()
        assert actual_message == expected_message, f"Mesajul de eroare obținut '{actual_message}' nu corespunde cu '{expected_message}'."


    def verify_success_message_text(self, expected_message):
        actual_message = self.get_succes_message_text()
        assert actual_message == expected_message, f"Mesajul de eroare obținut '{actual_message}' nu corespunde cu '{expected_message}'."


    def verify_password_error_message_text(self):
        actual_message = self.get_element_text(self.SECOND_PART_OF_THE_PASSWORD_ERROR)
        assert "must have at least 6 characters" in actual_message, "Mesajul nu contine textul asteptat"


    def verify_confirm_password_error_message_text(self, expected_message):
        actual_message = self.get_password_confirmation_error_message_text()
        assert actual_message == expected_message, f"Mesajul de eroare obținut '{actual_message}' nu corespunde cu '{expected_message}'."


    def verify_email_error_message_text(self, expected_message):
        actual_message = self.get_email_error_message_text()
        assert actual_message == expected_message, f"Mesajul de eroare obținut '{actual_message}' nu corespunde cu '{expected_message}'."