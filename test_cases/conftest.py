import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://iemodemoindia.meditab.com ")
    driver.implicitly_wait(5)
    return driver