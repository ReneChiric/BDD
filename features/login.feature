Feature: Test the functionality of the Login Page
#scenariul nr. 1 neparametrizat
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    Given I am on the Login Page
    When I insert an unregistered email in the email input
    When I insert a password in the password input
    When I Click login button
    Then the main error message is displayed
    Then The error text contains "No customer account found" message


#scenariul nr. 2 - parametrizat
  Scenario: Check that "No customer account found" message is displayed when the user tries to log in with an unregistered email
    Given I am on the Login Page
    When I insert "andsaj@host2.com" in the email input
    When I insert "2392094" in the password input
    When I Click login button
    Then the main error message is displayed
    Then The error text contains "No customer account found" message

#scenariul nr.3
  Scenario: Check that "Please enter your email" message is displayed when the user enters empty email address
    Given I am on the Login Page
    When I insert " " in the email input
    When I Click login button
    Then The mail error message is displayed
    Then The message is "Please enter your email"


#scenariul 4
  Scenario: Check that "Wrong Email" message is displayed when the user enters an invalid email format
    Given I am on the Login Page
    When I insert "emailinvalid" in the email input
    When I Click login button
    Then The mail error message is displayed
    Then The message is "Wrong email"

#scenariul nr. 5
  Scenario: Check that the Login Page Url is correct
    Given I am on the Login Page
    Then The URL is "https://demo.nopcommerce.com/login"

#scenariul nr.6
  Scenario: Check that when you click on the Forgot Password page the url is correct
    Given I am on the Login Page
    When I click Forgot Password
    Then The URL is "https://demo.nopcommerce.com/passwordrecovery"



