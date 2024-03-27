Feature: Test some of the functionalities of the Home Page

    Scenario: Check that "Please enter your email" message is displayed when the  user tries to subscribe with an invalid type e-mail
      Given I am on the Home Page
      When I click on Subscribe button without entering anything in the email input
      Then "Enter valid email" error is displayed


      Scenario: Check that Home Page URL is correct
        Given I am on the Home Page
        Then The URL is "https://demo.nopcommerce.com/"
