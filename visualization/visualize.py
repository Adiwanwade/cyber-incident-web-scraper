import sqlite3
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import pandas as pd
import geopandas as gpd
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt
from cartopy.io.img_tiles import OSM
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.img_tiles import Stamen


def fetch_incidents():
    conn = sqlite3.connect('data/cyber_incidents.db')
    cursor = conn.cursor()
    # cursor.execute("SELECT description, date FROM CyberIncidents")
    cursor.execute(
        "SELECT description, date,latitude,longitude FROM CyberIncidents")
    incidents = cursor.fetchall()
    conn.close()
    return incidents


def plot_incidents_over_time():
    incidents = fetch_incidents()
    if not incidents:
        print("No incident data available to plot.")
        return
    dates = [incident[1] for incident in incidents]
    unique_dates = len(set(dates))
    if unique_dates > 0:
        plt.hist(dates, bins=unique_dates)
        plt.xlabel('Date')
        plt.ylabel('Number of Incidents')
        plt.title('Cyber Incidents Over Time')
        plt.show()
    else:
        print("Not enough unique dates to create a histogram.")


def generate_word_cloud():
    incidents = fetch_incidents()
    if not incidents:
        print("No incident data available to generate word cloud.")
        return

    text = ' '.join([incident[0] for incident in incidents])
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Common Words in Cyber Incident Descriptions')
    plt.show()

    # Save the word cloud image
    wordcloud.to_file('cyber_incidents_wordcloud.png')
    print("Word cloud saved as 'cyber_incidents_wordcloud.png'.")


def plot_heatmap():
    incidents = fetch_incidents()
    if not incidents:
        print("No incident data available to plot heatmap.")
        return

    dates = [incident[1] for incident in incidents]
    sns.histplot(dates, bins=len(set(dates)), kde=True)
    plt.xlabel('Date')
    plt.ylabel('Number of Incidents')
    plt.title('Heatmap of Cyber Incidents Over Time')
    plt.show()


def plot_geospatial():
    incidents = fetch_incidents()
    if not incidents:
        print("No incident data available to plot geospatial map.")
        return

    fig = plt.figure(figsize=(12, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.coastlines()
    ax.gridlines(draw_labels=True)

    df = pd.DataFrame(incidents, columns=[
                      'description', 'date', 'latitude', 'longitude'])
    df = df.dropna(subset=['latitude', 'longitude'])

    lons = df['longitude'].to_numpy()
    lats = df['latitude'].to_numpy()

    ax.scatter(lons, lats, color='red', s=50,
               transform=ccrs.PlateCarree(), zorder=5, label='Cyber Incidents')

    plt.title('Geospatial Distribution of Cyber Incidents')
    plt.legend()
    plt.show()


def plot_network_graph():
    incidents = fetch_incidents()
    if not incidents:
        print("No incident data available to plot network graph.")
        return

    G = nx.Graph()
    for incident in incidents:
        G.add_node(incident[0])

        G.add_edges_from([(incident[0], other_incident[0])
                         for other_incident in incidents if incident != other_incident])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=50,
            node_color='blue', font_size=8)
    plt.title('Network Graph of Cyber Incidents')
    plt.show()


if __name__ == "__main__":
    generate_word_cloud()
    plot_incidents_over_time()
    plot_heatmap()
    plot_geospatial()
    plot_network_graph()
