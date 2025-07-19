import time
from page.world_population_pom import PopulationPage

def test_live_count (driver):
        page = PopulationPage(driver)
        page.total_population_count()
        time.sleep(10)
        print("Press CTRL+C to stop monitoring population count...")
        try:
            while True:
                count = page.total_population_count()
                print(f"Current Population Count: {count}", end="\r")
                time.sleep(1)  # Update every second
        except KeyboardInterrupt:
                print("\nMonitoring stopped by user.")