# Created by james at 1/15/2025
Feature: Tests for Reelly Main page UI

  Scenario: User can open the off plan page and go through the pagination
    Given Open Reelly main page
    Then Input email on SignIn page
    Then Input password on SignIn page
    Then Click Continue Button
    Then Verify Main Page Open
    Then Click off plan option
    Then Go to the final page using the pagination button
    Then Go back to the first page using pagination button
