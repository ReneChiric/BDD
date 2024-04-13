from behave import *

@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert an unregistered email in the email input')
def step_impl(context):
    context.login_page.set_unregistered_email()


@when('I insert "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I insert a password in the password input')
def step_impl(context):
    context.login_page.set_wrong_password()


@when('I insert "{password}" in the password input')
def step_impl(context, password):
    context.login_page.set_password(password)


@when('I Click login button')
def step_impl(context):
    context.login_page.click_login_btn()


@then('the main error message is displayed')
def step_impl(context):
    context.login_page.verify_main_error_message_displayed()


@then('The error text contains "No customer account found" message')
def step_impl(context):
    context.login_page.verify_unregistered_account_message_text()


@then('The error text contains "No customer account found"')
def step_impl(context):
    context.login_page.unregistered_account_message_displayed()


# @when('I insert " " in the email input')
# def step_impl(context):
#     context.login_page.set_email(' ')


@then('The mail error message is displayed')
def step_impl(context):
    context.login_page.is_email_error_message_displayed()


@then('The message is "{message}"')
def step_impl(context, message):
    context.login_page.verify_email_error_message_text(message)



@then('The URL is "{url}"')
def step_impl(context, url):
    context.login_page.is_url_correct(url)


@when('I click Forgot Password')
def step_impl(context):
    context.login_page.click_forgot_password_link()





