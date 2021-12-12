import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from Pages.SearchPage import SearchPage
from Pages.ResultPage import ResultPage

# CONST
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/login'


# Scenearios
# scenario('../features/Login.feature', scenario_name='Login in store webPage')

@scenario('../features/Search.feature', 'Search in store webPage')
def test_publish():
    pass


@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given
@given('the Store webPage')
def open_store_web(browser):
    browser.get(STORE_WEB)


@when(parsers.parse('search "{key}"'))
def complete_user_pass(browser, key):
    search_page = SearchPage(browser)

    search_page.getSearchInput().send_keys(key)
    search_page.getSearchBtn().click()


@then('product page is displayed')
def check_account(browser):
    print('Product page is displayed')
    result_page = ResultPage(browser)

    print( result_page.getTitle().text)

