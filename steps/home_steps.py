from behave import *

@given('I am on the Home Page')
def step_impl(context):
    context.home_page.navigate_to_home_page()


@when('I click on any vote option on the Community Poll section')
def step_impl(context):
    context.home_page.select_vote_option()


@when('I press "Vote" button')
def step_impl(context):
    context.home_page.click_on_vote_poll_button()


@then('The "Only registered users can vote" message is displayed')
def step_impl(context):
    assert context.home_page.is_vote_poll_error_message_displayed()


@when('I click on Subscribe button without entering anything in the email input')
def step_impl(context):
    context.home_page.click_on_subscribe_button()


@then('"Enter valid email" error is displayed')
def step_impl(context):
    assert context.home_page.is_subscribe_error_message_displayed()



