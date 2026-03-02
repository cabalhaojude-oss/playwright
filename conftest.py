import pytest
import os
import shutil

from pages.login_page import LoginPage
from utils.config import BASE_URL


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def login_page(page, base_url):
    login = LoginPage(page)
    login.goto(base_url)
    return login


@pytest.fixture(scope="session", autouse=True)
def setup_screenshots_folder():
    folder_path = "screenshots"

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

    os.makedirs(folder_path, exist_ok=True)
    yield