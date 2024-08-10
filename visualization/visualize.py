import sqlite3
import matplotlib.pyplot as plt

def fetch_incidents():
    conn = sqlite3.connect('data/cyber_incidents.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date FROM CyberIncidents")
    incidents = cursor.fetchall()
    conn.close()
    return incidents

def plot_incidents_over_time():
    incidents = fetch_incidents()
    if not incidents:
        print("No incident data available to plot.")
        return
    dates = [incident[0] for incident in incidents]
    unique_dates=len(set(dates))
    if unique_dates>0:
        plt.hist(dates, bins=len(set(dates)))
        plt.xlabel('Date')
        plt.ylabel('Number of Incidents')
        plt.title('Cyber Incidents Over Time')
        plt.show()
    else:
        print("Not enough unique dates to create a histogram.")

if __name__ == "__main__":
    plot_incidents_over_time()
