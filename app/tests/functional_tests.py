import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_homepage(driver):
    driver.get(os.getenv('HOMEPAGE'))
    expected = 'Dashboard'
    assert expected in driver.title