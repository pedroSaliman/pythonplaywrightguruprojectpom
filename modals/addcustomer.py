class AddCustomer:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("input[name='name']")
        self.gender = page.locator("input[value='f']")
        self.birth = page.locator("#dob")
        self.adress = page.locator("textarea[name='addr']")
        self.city = page.locator("input[name='city']")
        self.state = page.locator("input[name='state']")
        self.pin = page.locator("input[name='pinno']")
        self.mobilenumber = page.locator("input[name='telephoneno']")
        self.email = page.locator("input[name='emailid']")
        self.password = page.locator("input[name='password']")
        self.submit = page.locator("input[value='Submit']")



    
    def Addcust(self, thename,thebirth,theadress,thecity,thestate,thepin,themob,theemail,thepassword):
        self.username.fill(thename)
        self.gender.click()
        self.birth.fill(thebirth)
        self.adress.fill(theadress)
        self.city.fill(thecity)
        self.state.fill(thestate)
        self.pin.fill(thepin)
        self.mobilenumber.fill(themob)
        self.email.fill(theemail)
        self.password.fill(thepassword)
        self.submit.click()