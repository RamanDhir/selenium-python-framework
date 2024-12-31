#from base.selenium_driver import SeleniumDriver
import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.nav=NavigationPage(driver)

   # locators
    _login_link = "//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)

   # Actions on the locators

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email="", password=""):

        self.driver.refresh()
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

        # self.driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
        # self.driver.find_element(By.ID, "email").send_keys(username)
        # self.driver.find_element(By.ID, "login-password").send_keys(password)
        # self.driver.find_element(By.ID, "login").click()

    def verifyLoginSuccess(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[text()='Incorrect login details']",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        # if "Loginnnnnn" in self.getTitle():
        #     return True
        # else:
        #     return False
        return self.verifyPageTitle("My Courses")    # ----- this would pass in FIREFOX browser
        # return self.verifyPageTitle("Login")   ----- this would pass in CHROME browser

    def logout(self):
        self.nav.navigateToUserSettingsIcon()
        time.sleep(5)
        self.elementClick(locator="//a[@href='/logout']", locatorType="xpath")
