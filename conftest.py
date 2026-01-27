import pytest
from selene import Browser, Config
from selenium import webdriver

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    browser = Browser(Config(driver=driver, base_url='https://demoqa.com'))
    yield browser
    browser.quit()
