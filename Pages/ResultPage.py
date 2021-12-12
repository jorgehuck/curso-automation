from selenium.webdriver.common.by import By


class ResultPageLocators:
    TITLE = (By.CSS_SELECTOR, ".maintext")


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*ResultPageLocators.TITLE)
