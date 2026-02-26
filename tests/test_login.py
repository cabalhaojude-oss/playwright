from playwright.sync_api import expect

from pages.login_page import LoginPage
from functions.login_functions import LoginFunctions
from utils.test_data import VALID_USER, INVALID_USER

def test_valid_login(page, base_url):
    login_page = LoginPage(page)
    login_page.goto(base_url)
    login_actions = LoginFunctions(page)
    login_actions.login(VALID_USER["username"], VALID_USER["password"])

def test_invalid_login(page, base_url):
    login_page = LoginPage(page)
    login_page.goto(base_url)
    login_actions = LoginFunctions(page)
    login_actions.login(INVALID_USER["username"], INVALID_USER["password"])
