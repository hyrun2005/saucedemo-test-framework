class LoginPage:

    _loginLink = "https://www.saucedemo.com/"
    _usernameField = "input[id='user-name']"
    _passwordField = "input[id='password']"
    _submitButton = "input[type='submit']"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self._loginLink)

    def fill_form(self, username, password):
        self.page.locator(self._usernameField).fill(username)
        self.page.locator(self._passwordField).fill(password)

    def submit_form(self):
        self.page.locator(self._submitButton).click()

    def login(self, username, password):
        self.fill_form(username, password)
        self.submit_form()
