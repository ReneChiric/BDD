from behave import *

@given('I am on the Register Page')
def step_impl(context):
    context.register_page.navigate_to_register_page()

@when('I click on Register Button')
def step_impl(context):
    context.register_page.click_on_register_button()


@then('First Name Error is displayed')
def step_impl(context):
    context.register_page.verify_first_name_error_displayed()



@then('Last Name Error is displayed')
def step_impl(context):
    context.register_page.verify_last_name_error_displayed()


@then('Password Error is displayed')
def step_impl(context):
    context.register_page.verify_password_error_displayed()


@then('Confirm Password Error is displayed')
def step_impl(context):
    context.register_page.verify_confirm_password_error_displayed()


@when('I Introduce "{text}" in First Name Input')
def step_impl(context, text):
    context.register_page.set_first_name(text)


@when('I Introduce "{text}" in Last Name Input')
def step_impl(context, text):
    context.register_page.set_last_name(text)


@when('I Introduce "{email}" in the Email Input')
def step_impl(context, email):
    context.register_page.set_email(email)


@when('I Introduce "{password}" on Password Input')
def step_impl(context, password):
    context.register_page.set_password(password)


@when('I Introduce "{password}" on the Confirm Password Input')
def step_impl(context, password):
    context.register_page.set_confirm_password(password)


@then('The Success Message is displayed')
def step_impl(context):
    context.register_page.verify_succes_message_displayed()


@then('An Error for already used email is displayed')
def step_impl(context):
    context.register_page.verify_already_registered_email_error_displayed()


@then('Email error is displayed')
def step_impl(context):
    context.register_page.verify_email_error_displayed()


@then('The message text is "{message}"')
def step_impl(context, message):
    context.register_page.verify_success_message_text(message)


@then('The error message password text contains "must have at least 6 characters"')
def step_impl(context):
    context.register_page.verify_password_error_message_text()


@then('The error message text is "{error_message}"')
def step_impl(context, error_message):
    context.register_page.verify_confirm_password_error_message_text(error_message)


@then('Email error message is "{error_email_message}"')
def step_impl(context, error_email_message):
    context.register_page.verify_email_error_message_text(error_email_message)


@then('The error message for already used email is "{already_used_error}"')
def step_impl(context, already_used_error):
    context.register_page.verify_already_registered_email_error_text(already_used_error)