import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.courses.register_courses_pages import RegisterCoursePage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from selenium.webdriver.support import expected_conditions as EC
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()
        # WebDriverWait(self.driver, 10).until(
        #     EC.invisibility_of_element_located((By.CLASS_NAME, "blockOverlay"))
        # )
        # link_element = self.driver.find_element(By.XPATH, "//li[@data-id='41189']//a")
        # link_element.click()

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:/workspace_python/letskodeit/letskodeit/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        time.sleep(1)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result=result, resultMessage="Enrollment FAILED Verification")
