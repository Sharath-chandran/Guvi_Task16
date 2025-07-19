# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
        driver = webdriver.Chrome()
        driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")
        driver.maximize_window()
        yield driver
        driver.quit()