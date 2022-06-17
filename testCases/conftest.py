from selenium import webdriver
import pytest

# @pytest.fixture()

# def setup():
#     driver=webdriver.Chrome(executable_path="C:\\browser\\chromedriver.exe")
#     return driver
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="C:\\browser\\chromedriver.exe")
        print("Launching Chrome Browser")

    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="C:\\browser\\geckodriver.exe")
        print("Launchinf Firefox browser")

    else:
        driver=webdriver.Ie()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#############  Pytest HTML Report ##################
def pytest_configure(config):
    config._metadata['Project Name']='nop Comerce'
    config._metadata['Module name']='Customers'
    config._metadata['Tester']='Lucifer'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_meatdata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


