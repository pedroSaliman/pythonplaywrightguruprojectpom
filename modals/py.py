class LoginPage:
    def __init__(self, page):
        self.page = page
        self.userid = page.locator("input[name='uid']")
        self.passworduser = page.locator("input[name='password']")
        self.btn = page.locator("input[value='LOGIN']")



    def navigate(self):
        self.page.goto("https://demo.guru99.com/v4/index.php")

    def search(self, text,password):
        self.userid.fill(text)
        self.passworduser.fill(password)
        self.btn.click()