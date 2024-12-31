#from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver

   # locators
    _home_page_link = "//li[@data-id='41188']//a"
    _all_courses = "//li[@data-id='41189']//a"
    _my_courses = "//a[@href='/mycourses']"
    _user_settings_icon = "//button[@id='dropdownMenu1']"
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

    def navigateToHomePage(self):
        self.elementClick(locator=self._home_page_link, locatorType="xpath")

    def navigateToAllCourses(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "blockOverlay"))
        )
        link_element = self.driver.find_element(By.XPATH, "//li[@data-id='41189']//a")
        link_element.click()
        # self.elementClick(locator=self._all_courses, locatorType="xpath")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="xpath")

    def navigateToUserSettingsIcon(self):
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")

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
        return self.verifyPageTitle("Incorrect_title")