from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# POM class named PopulationPage.
# It encapsulates the logic to retrieve the population count from a web page
class PopulationPage:

    # Initializes the PopulationPage class with a WebDriver instance.
    # And defines a locator for the population count element using XPath.
    def __init__(self, driver):
        self.driver = driver
        self.population_count = (By.XPATH, "//*[@id='content']/div/div/app-page/header/app-asset-title/section/div/app-counter/div/div[1]")

    # Method to Get Population Count
    def total_population_count(self):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(self.population_count))
        # * unpacks the tuple (By.XPATH, "locator") into find_element(By.XPATH, "locator")
        return self.driver.find_element(*self.population_count).text