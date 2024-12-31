from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.basepage import BasePage
import logging
import utilities.custom_logger as cl

class RegisterCoursePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    # locators
    _all_courses = "//li[@data-id='41189']//a"                                              # locator = xpath
    _search_box = "//input[@placeholder='Search Course']"                                # locator = xpath
    _search_button= "//button[@type='submit']"                                              # locator = xpath
    _course="//h4[contains(@class, 'dynamic-heading') and contains(text(), '{0}')]"  # locator = xpath
    _all_course_title = "//h4[@class='dynamic-heading']"                                    # locator = xpath
    _enroll_button = "//button[contains(text(),'Enroll in Course')]"                        # locator = xpath
    _cc_num = "input[placeholder='Card Number']"    # locator = css
    _cc_exp = "input[placeholder='MM / YY']"                                              # locator = css
    _cc_cvv = "input[placeholder='Security Code']"                                          # locator = css
    _submit_enroll = "//button[contains(@class,'sp-buy')]//i[contains(@class, 'fa-arrow-right')]"   # locator = xpath
    _enroll_error_message = "//button[@data-dismiss='alert']/.."             # message="Your card number is incorrect."

    # DUMMY card details here: https://developers.bluesnap.com/reference/test-credit-cards

    def enterCourseName(self, name):
        # Line numbers 36-41: we are clicking on 'All Courses' button and this button is hidden, hence used below logic.
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "blockOverlay"))
        )

        link_element = self.driver.find_element(By.XPATH, "//li[@data-id='41189']//a")
        link_element.click()

        # print("Element ID is: "+str(element4))
        # self.waitForElement(element4, locatorType="xpath")
        # mouseAction = ActionChains(self.driver)
        # mouseAction.move_to_element(element4).click().perform()


        # element4.click()
        # self.elementClick(locator=self._all_courses, locatorType="xpath")
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "blockOverlay"))
        )
        self.sendKeys(data=name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_button, locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):

        # Tutor's approach ######################

        self.switchToFrameDynamicXpath(locator="//iframe[contains(@name, '__privateStripeFrame')]", locatorType="xpath")
        self.sendKeys(num, locator=self._cc_num, locatorType="CSS")
        self.switchToDefaultContent()

        # Tutor's approach ######################



    # My approach (which is working) ######################

        # # Faced below issues:
        # # 1. Card number text box is in the iframe.
        # # 2. iframe name is dynamic
        # # 3. we need to wait for iframe to load.
        #
        # try:
        #     iframe = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, '__privateStripeFrame')]"))
        #     )
        #     self.driver.switch_to.frame(iframe)
        #
        #     # Wait for input field and enter data
        #     card_number_input = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Card Number']"))
        #     )
        #     card_number_input.send_keys(num)
        #     print("Card number entered successfully.")
        #
        #     # Switch back to the main content
        #     self.driver.switch_to.default_content()
        #
        # except Exception as e:
        #     print("An error occurred:", str(e))

    # My approach (which is working) ######################

    def enterCardExp(self, exp):

        # Tutor's approach ######################

        self.switchToFrameDynamicXpath(locator="//div[@id='card-expiry']//iframe[contains(@name, '__privateStripeFrame')]", locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="CSS")
        self.switchToDefaultContent()

        # Tutor's approach ######################

        # My approach (which is working) ######################

        # try:
        #     iframe = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, "//div[@id='card-expiry']//iframe[contains(@name, '__privateStripeFrame')]"))
        #     )
        #     self.driver.switch_to.frame(iframe)
        #
        #     # Wait for input field and enter data
        #     exp_date_input = WebDriverWait(self.driver, 10).until(
        #             EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='MM / YY']"))
        #     )
        #     exp_date_input.send_keys(exp)
        #     print("Expiry date entered successfully.")
        #
        #     # Switch back to the main content
        #     self.driver.switch_to.default_content()
        #
        # except Exception as e:
        #     print("UNABLE TO ENTER card expiry date")
        #     print("An error occurred:", str(e))

        # My approach (which is working) ######################

    def enterCardCVV(self,cvv):

        # Tutor's approach ######################

        self.switchToFrameDynamicXpath(locator="//div[@id='card-cvc']//iframe[contains(@name, '__privateStripeFrame')]", locatorType="xpath")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="CSS")
        self.switchToDefaultContent()

        # Tutor's approach ######################

        # My approach (which is working) ######################

        # try:
        #     iframe = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, "//div[@id='card-cvc']//iframe[contains(@name, '__privateStripeFrame')]"))
        #     )
        #     self.driver.switch_to.frame(iframe)
        #
        #     # Wait for input field and enter data
        #     card_cvv_input = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Security Code"))
        #     )
        #     card_cvv_input.send_keys(cvv)
        #     print("CVV entered successfully.")
        #
        #     # Switch back to the main content
        #     self.driver.switch_to.default_content()
        #
        # except Exception as e:
        #     print("UNABLE TO ENTER cvv")
        #     print("An error occurred:", str(e))

        # My approach (which is working) ######################

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp,cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        # scroll down to the bottom of the page to enter card details
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        self.webScroll(direction="up")
        messageElement = self.waitForElement(locator=self._enroll_error_message, locatorType="xpath")
        # result=self.isElementDisplayed(element=messageElement)
        result= self.isElementDisplayed(locator=self._enroll_error_message, locatorType="xpath")
        return result