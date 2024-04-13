from behave import *


@when('The user types "{text}" in the search input')
def step_impl(context, text):
    context.home_page.type_text_on_search_input(text)

@when('The user clicks on Search Button')
def step_impl(context):
    context.home_page.click_search_button()

@then('Search results are displayed')
def step_impl(context):
    context.search_results_page.are_all_products_displayed()

@then('All the search results contains the word "{text}"')
def step_impl(context, text):
    context.search_results_page.are_all_titles_containing_text(text)


