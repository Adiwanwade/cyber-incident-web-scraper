from scripts.store_data import store_incidents
from scripts.store_data import update_table_schema
from visualization.visualize import plot_incidents_over_time
from visualization.visualize import generate_word_cloud
from visualization.visualize import plot_heatmap
from visualization.visualize import plot_geospatial
from visualization.visualize import plot_network_graph
from scripts.scraper import scrape_all
from scripts.ml_platform_identifier import identify_cyber_platform
def main():
    # Step 1: Scrape data and store in database
    incidents=scrape_all()
    store_incidents(incidents)
    update_table_schema()
    # Step 2: Visualize data
    generate_word_cloud()
    plot_incidents_over_time()
    plot_heatmap()
    plot_geospatial()
    plot_network_graph()
    # identify_cyber_platform()
if __name__ == "__main__":
    main()