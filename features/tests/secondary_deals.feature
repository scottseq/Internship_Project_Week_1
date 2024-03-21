# Created by SSCOTT at 3/13/2024
Feature: User can filter the Secondary deals by “want to sell” option
  # Enter feature description here

  Scenario: secondary deals
    Given Open the main page
    Then Log in to the page
    When Click on "secondary" option at the left side of the page
    Then Verify the right page opens
    When Filter the products by "want to sell"
    Then Verify all cards have "for sale" tag


    # Enter steps here