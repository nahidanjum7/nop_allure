import pytest
from selenium import webdriver
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def setup(request):
    browser=request.config.getoption("--browser")

    if browser=="chrome":
        print("Test Run- Browser Chrome")
        driver=webdriver.Chrome()

    elif browser=="edge":
        print("Test Run- Browser Edge")
        driver = webdriver.Edge()

    elif browser=="firefox":
        print("Test Run- Browser Firefox")
        driver = webdriver.Firefox()

    else:
        print("Test Run- Browser Headless\n")
        driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://admin-demo.nopcommerce.com/")
    # driver.implicitly_wait(5)
    driver.maximize_window()
    # return driver
    yield driver #return driver otherwise this is compusory required
    driver.quit()

@pytest.fixture(params=[
    ("admin@yourstore.com", "admin", "Pass"),
    ("admin@yourstore.com", "admin1", "Fail"),
    ("admin@yourstore.com1", "admin", "Fail"),
    ("admin@yourstore.com1", "admin1", "Fail")
])
def DataForLogin(request):
    return request.param








