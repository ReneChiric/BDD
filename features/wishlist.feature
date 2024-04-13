Feature: Test some functionalities of the Wishlist Page
  Scenario: Check that "The wishlist is empty!" message is displayed if the user goes directly from the Home Page to the Wishlist Page
    Given I am on the Wishlist Page
    Then The "Wishlist is empty!" message is displayed

  Scenario: Check that WishList Page URL is correct
    Given I am on the Wishlist Page
    Then The URL is "https://demo.nopcommerce.com/wishlist"


