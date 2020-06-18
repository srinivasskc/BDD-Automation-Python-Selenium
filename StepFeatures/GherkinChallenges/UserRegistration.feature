Feature: User Registration Functionality

  Background: Given User is on Registration Page

  @smoke
  Scenario Outline: User Registration with User that does not exists in repository
    When User enters username "<username>"
    And User enters email id "<email id>"
    And User enters password "<password>"
    And User clicks on Sign Up Button
    Then User should be registered successfully

    Examples:
      |username| |email id| |password|
      |srinivas| |sk@gmail.com| |sk@madeIn|
      |srini   | |sr@gmail.com| |sr@InMade|


  @sanity @smoke
  Scenario: User Registration with User already exists in repository
    When User enters username "srinivas" which exists
    And User enters email id "sk@gmail.com"
    And User enters password "sk@madeIn"
    And User clicks on Sign Up Button
    Then User should not be registered successfully.