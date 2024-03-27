from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    VOTE_POLL_BUTTON = (By.ID, 'vote-poll-1')
    VOTE_POLL_ERROR_MESSAGE = (By.CLASS_NAME, 'poll-vote-error')
    NEWSLETTER_BUTTON_INPUT_BOX = (By.ID, 'newsletter-email')
    SUBSCRIBE_BUTTON = (By.ID, 'newsletter-subscribe-button')
    SUBSCRIBE_EMAIL_ERROR_MESSAGE = (By.CLASS_NAME, 'newsletter-subscribe-text')
    SELECT_VOTE_OPTION_1 = (By.ID, 'pollanswers-1')


    def navigate_to_home_page(self):
        self.driver.get(self.base_Url)

    def is_vote_poll_error_message_displayed(self):
        return self.is_element_displayed(self.VOTE_POLL_ERROR_MESSAGE)

    def click_on_vote_poll_button(self):
        self.click(self.VOTE_POLL_BUTTON)

    def get_vote_poll_error_message_text(self):
        return self.get_element_text(self.VOTE_POLL_ERROR_MESSAGE)

    def click_on_subscribe_button(self):
        self.click(self.SUBSCRIBE_BUTTON)

    def type_on_newsletter_button_an_invalid_type_email(self, invalid_email):
        self.type(self.NEWSLETTER_BUTTON_INPUT_BOX, invalid_email)

    def select_vote_option(self):
        self.click(self.SELECT_VOTE_OPTION_1)

    def is_subscribe_error_message_displayed(self):
        return self.is_element_displayed(self.SUBSCRIBE_EMAIL_ERROR_MESSAGE)

    def get_subscribe_error_message_text(self):
        return self.get_element_text(self.SUBSCRIBE_EMAIL_ERROR_MESSAGE)
