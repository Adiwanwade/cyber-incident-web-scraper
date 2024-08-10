from scripts.store_data import store_incidents
from visualization.visualize import plot_incidents_over_time
from scripts.scraper import scrape_all
def main():
    # Step 1: Scrape data and store in database
    incidents=scrape_all()
    store_incidents(incidents)
    # Step 2: Visualize data
    plot_incidents_over_time()

if __name__ == "__main__":
    main()