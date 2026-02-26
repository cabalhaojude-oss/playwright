import pytest
from playwright.sync_api import expect

from utils.test_data import VALID_USER, INVALID_USERNAME, INVALID_PASSWORD

@pytest.mark.valid_login
def test_valid_login(login_page, page):
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    expect(page.get_by_text("Logged In Successfully")).to_be_visible()
    # page.screenshot(path= "success_login_screenshot.png")

@pytest.mark.invalid_login
def test_invalid_username(login_page, page):
    login_page.login(INVALID_USERNAME["username"], INVALID_USERNAME["password"])
    expect(page.locator("#error")).to_contain_text("Your username is invalid!")
    # page.screenshot(path= "invalid_username_screenshot.png")

@pytest.mark.invalid_login
def test_invalid_password(login_page, page):
    login_page.login(INVALID_PASSWORD["username"], INVALID_PASSWORD["password"])
    expect(page.locator("#error")).to_contain_text("Your password is invalid!")
    # page.screenshot(path="invalid_username_screenshot.png")

