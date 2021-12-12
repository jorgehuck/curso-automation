import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from Pages.LoginPage import LoginPage

# CONST
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/login'


# Scenearios
# scenario('../features/Login.feature', scenario_name='Login in store webPage')

@scenario('../features/Login.feature', 'Login in store webPage')
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


@when(parsers.parse('complete "{username}" and "{password}"'))
def complete_user_pass(browser, username, password):
    login_page = LoginPage(browser)

    login_page.getUserInput().send_keys(username)
    login_page.getPassInput().send_keys(password)
    login_page.getLoginBtn().click()


@then('my account page is displayed')
def check_account(browser):
    print('Account page is displayed')
