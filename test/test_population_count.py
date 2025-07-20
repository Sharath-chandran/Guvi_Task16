import time
from page.world_population_pom import PopulationPage

def test_live_count (driver):
        # Creates an instance of the PopulationPage
        page = PopulationPage(driver)
        page.total_population_count()
        time.sleep(10)

        # Continuous Monitoring Loop
        print("Press CTRL+C to stop monitoring population count...")

        #  infinite loop to continuously fetch the live population count
        try:
            while True:
                count = page.total_population_count()
                # updates the console in-place — simulates a live feed effect.
                print(f"Current Population Count: {count}", end="\r")
                time.sleep(1)  # Update every second

        # Exit with KeyboardInterrupt
        # loop keeps running until you manually stop it by pressing CTRL+C.
        except KeyboardInterrupt:
                print("\nMonitoring stopped by user.")