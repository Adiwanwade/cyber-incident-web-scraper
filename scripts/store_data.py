import sqlite3
from scripts.scraper import scrape_all

def store_incidents(incidents):
    conn = sqlite3.connect('data/cyber_incidents.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS CyberIncidents
                      (id INTEGER PRIMARY KEY, title TEXT, date TEXT, description TEXT, platform TEXT)''')

    for incident in incidents:
        cursor.execute('INSERT INTO CyberIncidents (title, date, description, platform) VALUES (?, ?, ?, ?)',
                       (incident['title'], incident['date'], incident['description'], 'example.com'))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    example_incidents=[
        {'title':'Example Incident','date':'2024-08-09','description':'This is a sample incident','platform':'example.com'}
    ]
    store_incidents(example_incidents)