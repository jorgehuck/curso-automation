from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.ID, 'filter_keyword')
    SEARCH_BTN = (By.CSS_SELECTOR, 'input#filter_keyword')
    RESULT_LINK = (By.CSS_SELECTOR, "a[title = 'Absolue Eye Precious Cells']")


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def getSearchInput(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_INPUT)

    def getSearchBtn(self):
        return self.driver.find_element(*SearchPageLocators.SEARCH_BTN)

    def getResultLink(self):
        return self.driver.find_element(*SearchPageLocators.RESULT_LINK)
