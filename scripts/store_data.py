import sqlite3
from scripts.scraper import scrape_all


def create_table_if_not_exists():
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS CyberIncidents
                      (id INTEGER PRIMARY KEY, title TEXT, date TEXT, description TEXT, platform TEXT, latitude REAL, longitude REAL)''')
    
    conn.commit()
    conn.close()

def update_table_schema():
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Ensure table exists before altering it
    cursor.execute("PRAGMA table_info(CyberIncidents)")
    columns = [column[1] for column in cursor.fetchall()]

    if 'latitude' not in columns:
        cursor.execute('''ALTER TABLE CyberIncidents ADD COLUMN latitude REAL''')
        print("Column 'latitude' added.")
    else:
        print("Column 'latitude' already exists.")

    conn.commit()
    conn.close()

def store_incidents(incidents):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Ensure table exists before inserting
    cursor.execute('''CREATE TABLE IF NOT EXISTS CyberIncidents
                      (id INTEGER PRIMARY KEY, title TEXT, date TEXT, description TEXT, platform TEXT, latitude REAL, longitude REAL)''')

    for incident in incidents:
        title = incident.get('title', 'N/A')
        date = incident.get('date', 'N/A')
        description = incident.get('description', 'N/A')
        latitude = incident.get('latitude', None)
        longitude = incident.get('longitude', None)

        cursor.execute('INSERT INTO CyberIncidents (title, date, description, platform, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)',
                       (title, date, description, 'example.com', latitude, longitude))

    conn.commit()
    conn.close()

if __name__ == "__main__":
   
    create_table_if_not_exists()
    update_table_schema()

    # Scrape and store incidents
    incidents = scrape_all()
    store_incidents(incidents)