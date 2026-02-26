import os
from datetime import datetime

class Common:

    def __init__(self, page):
        self.page = page

    # -----------------------
    # Navigation & Waits
    # -----------------------

    def wait_for_selector(self, locator, timeout=5000):
        self.page.locator(locator).wait_for(timeout=timeout)

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")

    # -----------------------
    # Screenshots
    # -----------------------

    def take_screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/{name}_{timestamp}.png"
        self.page.screenshot(path=path, full_page=True)
        return path

    # -----------------------
    # Scrolling & Hover
    # -----------------------

    def scroll_to(self, locator):
        self.page.locator(locator).scroll_into_view_if_needed()

    def hover(self, locator):
        self.page.locator(locator).hover()

    # -----------------------
    # Alerts & Dialogs
    # -----------------------

    def accept_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

    def dismiss_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())

    # -----------------------
    # URL & Title
    # -----------------------

    def get_current_url(self):
        return self.page.url

    def get_title(self):
        return self.page.title()
