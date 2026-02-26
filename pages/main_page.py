from utils.common import Common

class MainPage(Common):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)
