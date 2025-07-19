# world_population
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PopulationPage:

    def __init__(self, driver):
        self.driver = driver
        self.population_count = (By.XPATH, "//*[@id='content']/div/div/app-page/header/app-asset-title/section/div/app-counter/div/div[1]")

    def total_population_count(self):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(self.population_count))
        return self.driver.find_element(*self.population_count).text