class LoginPage:

    __loginLink = "https://www.saucedemo.com/"
    __usernameField = "input[id='user-name']"
    __passwordField = "input[id='password']"
    __submitButton = "input[type='submit']"

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(self.__loginLink)

    def fill_form(self, username, password):
        self.page.locator(self.__usernameField).fill(username)
        self.page.locator(self.__passwordField).fill(password)

    def submit_form(self):
        self.page.locator(self.__submitButton).click()

    def login(self, username, password):
        self.fill_form(username, password)
        self.submit_form()