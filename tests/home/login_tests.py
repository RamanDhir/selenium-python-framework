import time

from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        print("########### In test_validLogin METHOD ###########")
        self.lp.login("raman.dhir1991@gmail.com", "kodeIt@123")
        print("########### verifing the PAGE TITLE ###########")
        time.sleep(3)
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_validLogin", result2, "Login was SUCCESSFUL")


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("TTTTTTTT@gmail.com", "12344555")
        result = self.lp.verifyLoginFailed()
        assert result == True

# lt=LoginTests()
# lt.test_validLogin()