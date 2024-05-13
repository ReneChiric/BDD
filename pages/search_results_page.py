from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    PRODUCT_ITEM = (By.CLASS_NAME, "product-item")
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")

    def are_all_products_displayed(self):
        self.wait_for_element_to_be_present(self.PRODUCT_ITEM, 3)
        product_list = self.find_all(self.PRODUCT_ITEM) #cream lista pentru produsele

        for product in product_list:   #iteram prin lista
            if not product.is_displayed(): #
                raise AssertionError

        return True

    def are_all_titles_containing_text(self, text: str): #conditionam ca parametrul sa fie de tipul string
        titles_list = self.find_all(self.PRODUCT_TITLE)

        for title in titles_list:
            if text.lower() not in title.text.lower():
                raise AssertionError

        return True




