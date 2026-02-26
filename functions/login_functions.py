from pages.login_page import LoginPage


class LoginFunctions(LoginPage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
