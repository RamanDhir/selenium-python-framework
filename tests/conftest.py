import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running ONE TIME setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp= LoginPage(driver)
    print("########### In oneTimeSetUp METHOD ###########")
    lp.login("raman.dhir1991@gmail.com", "kodeIt@123")
    print("########### LOGGED IN using oneTimeSetUp METHOD ###########")
    # if browser == "firefox":
    #     baseUrl = "https://www.letskodeit.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseUrl)
    #     print("Running tests on FF")
    #     driver.refresh()
    # else:
    #     baseUrl = "https://www.letskodeit.com/"
    #     driver=webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseUrl)
    #     print("Running tests on CHROME")
    #     driver.refresh()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    # driver.quit()
    print("Running ONE TIME tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")