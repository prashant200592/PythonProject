import pytest
from selenium import webdriver
from datetime import datetime
import os

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

def pytest_html_report_title(report):
    report.title = "Automation Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Tester: Prashant"
    ])

def pytest_metadata(metadata,config):
    metadata.pop("JAVA_HOME", None)
    metadata["Project"]:"Automation Test Project"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir+"\\reports\\"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html")



