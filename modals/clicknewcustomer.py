class NewCustomerPage:
    def __init__(self, page):
        self.page = page
        self.customer = page.locator("a[href='addcustomerpage.php']")
   
    def search(self):
      
        self.customer.click()