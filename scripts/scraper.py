import requests
from bs4 import BeautifulSoup
from config.config import SCRAPER_URLS

def fetch_cyber_incidents(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        incidents = []

        # Example extraction logic
        for incident in soup.find_all('div', class_='incident-entry'):
            title = incident.find('h2').get_text()
            date = incident.find('span', class_='date').get_text()
            description = incident.find('p').get_text()
            incidents.append({'title': title, 'date': date, 'description': description})
        
        return incidents
    else:
        print("Failed to retrieve content")
        return []
    # incidents=[
    #     {'title':'Sample Cyber Attack 1','date':'2024-08-01','description':'This is a description of a sample cyber attack.'},
    #     {'title':'Sample Cyber Attack 2','date':'2024-08-03','description':'This is a description of another sample cyber attack.'},
    # ]
    # return incidents

def scrape_all():
    all_incidents = []
    for url in SCRAPER_URLS:
        incidents = fetch_cyber_incidents(url)
        all_incidents.extend(incidents)
    return all_incidents

if __name__ == "__main__":
    incidents = scrape_all()
    print(incidents)