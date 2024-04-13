Feature: Test some functionalities of the Search Functionality
  Scenario: Check that the user can use the Search Function
    Given I am on the Home Page
    When The user types "laptop" in the search input
    When The user clicks on Search Button
    Then Search results are displayed
    Then All the search results contains the word "laptop"

    Scenario Outline:
      Given I am on the Home Page
      When The user types "<text>" in the search input
      When The user clicks on Search Button
      Then Search results are displayed
      Then All the search results contains the word "<text>"

      Examples:
        | text         |
        | HTC          |
        | Bracelet     |
        | Flower       |
        | Ring         |
        | Phone        |
        | Ray Bradbury |





