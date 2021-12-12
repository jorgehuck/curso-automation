Feature: Login in Store
  As a user
  I want to access the Store page
  So Login correctly

  Scenario: Login in store webPage
    Given the Store webPage
    When complete "agusDarwoft" and "automation"
    Then my account page is displayed