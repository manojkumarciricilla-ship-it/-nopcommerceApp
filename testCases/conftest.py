# from selenium import webdriver
# import pytest
#
# @pytest.fixture()
# def setup(browser):
#   if browser == 'chrome':
#       driver =webdriver.Chrome()
#       print("Launching chrome browser.....")
#   elif browser == 'firefox':
#       driver = webdriver.Firefox()
#       print("Launching Firefox browser.....")
#   else:
#       driver = webdriver.Ie()
#   return driver
#
#
# def pytest_addoption(parser):  # this will get the value from CLI /hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# ###########pytest HTML Report ####################
#
# # It is ook for environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Manoj'
#
# # It is hook for delete/modify Environment info to HTML report
# @pytest.mark.optionallhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#
#
import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    elif browser == 'ie':
        driver = webdriver.Ie()
        print("Launching Internet Explorer browser...")
    else:
        raise Exception(f"Browser not supported: {browser}")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type: chrome, firefox, or ie")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ✅ Works with pytest-html >= 4.0
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "nopCommerce Test Report"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name: nopCommerce | ",
        "Module: Customers | ",
        "Tester: Manoj"
    ])
