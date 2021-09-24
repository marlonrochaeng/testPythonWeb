import pytest
from selenium import webdriver

driver = None

@pytest.fixture(scope='function')
def BrowserSetUp(request, browser):
    global driver
    print("Running browser setUp")

    if browser == 'firefox':
        print("Tests will be executed on Firefox")
        driver = webdriver.Firefox()

    elif browser =='chrome':
        print("Tests will be executed on Chrome")
        driver = webdriver.Chrome("config/chromedriver.exe")

    elif browser == 'safari':
        driver = webdriver.Safari()

    driver.maximize_window()
    driver.implicitly_wait(20)

    if request.cls:
        request.cls.driver = driver

    yield driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")