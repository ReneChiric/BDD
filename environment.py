
from browser import Browser
from pages.home_page import HomePage

from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage
from pages.wishlist_page import WishlistPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.home_page = HomePage()
    context.wishlist_page = WishlistPage()
    context.search_results_page = SearchResultsPage()
    context.register_page = RegisterPage()


def after_all(context):
    context.browser.close()