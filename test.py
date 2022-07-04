from playwright.sync_api import Page
from modals.py import LoginPage
from modals.clicknewcustomer import NewCustomerPage
from modals.addcustomer import AddCustomer
from pages import element
import pytest
@pytest.fixture(autouse=True)
def setup(page:Page):
    Login=LoginPage(page)
    Login.navigate()


####################################################
def test_1(page:Page):
    Login = LoginPage(page)
    Login.search(element.userId,element.userPass)
#####################################################
def test_2(page:Page):
     Login = LoginPage(page)
     Login.search(element.userId,element.userPass)
     Customer=NewCustomerPage(page)
     Customer.search()
     Add= AddCustomer(page)
     Add.Addcust(element.User,element.Birth,element.Adress,element.City,element.State,element.Pin,element.Mobile,element.Email,element.Password)
####################################################

    