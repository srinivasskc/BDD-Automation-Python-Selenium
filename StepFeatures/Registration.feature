Feature: Verifying Registration Functionality

  @smoke
  Scenario: Registration with Valid Data
    Given User is on Registration Page
    When User enters username
    And User enters email id
    And User enters password
    And User clicks on Sign Up Button
    Then User should be registered successfully

  @sanity @smoke
  Scenario: Registration with Duplicate Username
    Given User is on Registration Page
    When User enters duplicate username
    And User enters email id
    And User enters password
    And User clicks on Sign Up Button
    Then User should not be registered successfully.



