from behave import *

@given('I am on the Wishlist Page')
def step_impl(context):
    context.wishlist_page.navigate_to_wishlist_page()


@then('The "Wishlist is empty!" message is displayed')
def step_impl(context):
    context.wishlist_page.verify_wishlist_message_displayed()


@when('I select "Add to Wishlist" option')
def step_impl(context):
    context.wishlist_page.add_to_wishlist()


@when('I navigate to Wishlist Page')
def step_impl(context):
    context.wishlist_page.navigate_to_wishlist_page()


@then('The wishlist is populated')
def step_impl(context):
    context.wishlist_page.is_wishlist_populated()