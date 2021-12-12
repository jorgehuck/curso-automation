Feature: Search in Store
  As a visitor
  I want to search in the Store a product by key 'Absolue Eye Precious Cells'
  So Found the product

  Scenario: Search in store webPage
    Given the Store webPage
    When search "Absolue Eye Precious Cells"
    Then product page is displayed