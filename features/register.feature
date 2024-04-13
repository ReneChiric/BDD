Feature: Check the functionality of the Register Page

  Background:
    Given I am on the Register Page


  Scenario: Check that when user clicks on Register Button without completing any field, all the errors are displayed
    When I click on Register Button
    Then First Name Error is displayed
    Then Last Name Error is displayed
    Then Password Error is displayed
    Then Email error is displayed
    Then Confirm Password Error is displayed


    Scenario: Check that success message is displayed when the user completes the registration with minimum info
      When I Introduce "Popescu" in First Name Input
      When I Introduce "Antonio" in Last Name Input
      When I Introduce "email@emainll23.com" in the Email Input
      When I Introduce "123456" on Password Input
      When I Introduce "123456" on the Confirm Password Input
      When I click on Register Button
      Then The Success Message is displayed
      Then The message text is "Your registration completed"


      Scenario: Check that the user cannot register with the same email if the email was used before
        When I Introduce "Popescu" in First Name Input
        When I Introduce "Antonio" in Last Name Input
        When I Introduce "email@emainll23.com" in the Email Input
        When I Introduce "123456" on Password Input
        When I Introduce "123456" on the Confirm Password Input
        When I click on Register Button
        Then An Error for already used email is displayed
        Then The error message for already used email is "The specified email already exists"


        Scenario: Check that the user cannot register if he types an invalid type email and receives an email error message
          When I Introduce "Popescu" in First Name Input
          When I Introduce "Antonio" in Last Name Input
          When I Introduce "emails" in the Email Input
          When I Introduce "123456" on Password Input
          Then Email error is displayed
          Then Email error message is "Wrong email"


          Scenario: Check that the user cannot type an invalid password format with less than 6 characters and receives an email error message
            When I Introduce "Popescu" in First Name Input
            When I Introduce "Antonio" in Last Name Input
            When I Introduce "emailoarecare@email2371233.com" in the Email Input
            When I Introduce "12346" on Password Input
            When I Introduce "123456" on the Confirm Password Input
            Then Password Error is displayed
            Then The error message password text contains "must have at least 6 characters"


            Scenario: Check that error is displayed when the password do no match
              When I Introduce "Popescu" in First Name Input
              When I Introduce "Antonio" in Last Name Input
              When I Introduce "emailoarecare@email23712333.com" in the Email Input
              When I Introduce "123456" on Password Input
              When I Introduce "1234567" on the Confirm Password Input
              When I click on Register Button
              Then Confirm Password Error is displayed
              Then The error message text is "The password and confirmation password do not match."




