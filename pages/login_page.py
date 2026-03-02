from pages.main_page import MainPage


class LoginPage(MainPage):

    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Submit")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


