import requests
from bs4 import BeautifulSoup
import re
from config.config import SCRAPER_URLS

# Function to fetch and parse the content of a URL
def fetch_content(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Failed to retrieve content from {url}")
        return None

# Function to search for cyber-related keywords in the content
def search_cyber_incidents(soup):
    keywords = ["cyber", "cybercrime", "cybersecurity", "hacking", "data breach"] # Could add more keywords
    incidents = []

    for keyword in keywords:
        for tag in soup.find_all(text=re.compile(keyword, re.IGNORECASE)):
            parent = tag.find_parent()
            if parent:
                title = parent.get_text(strip=True)
                date = parent.find_previous('time')
                location = parent.find_previous('span', class_='location')
                date_text = date.get_text(strip=True) if date else "No date available"
                incidents.append({'title': title, 'date': date_text, 'description': title, 'location': location})

    return incidents

# Function to scrape all URLs and return the incidents
def scrape_all():
    all_incidents = []
    for url in SCRAPER_URLS:
        soup = fetch_content(url)
        if soup:
            incidents = search_cyber_incidents(soup)
            if incidents:
                print(f"Incidents fetched from {url}:")
                for incident in incidents:
                    print(f"Title: {incident.get('title')}")
                    print(f"Date: {incident.get('date')}")
                    print(f"location: {incident.get('location')}")
                    print(f"Description: {incident.get('description')}\n")
                    # print('found')
            else:
                print(f"No incidents found from {url}.")
            all_incidents.extend(incidents)
        else:
            print(f"Failed to fetch content from {url}.")
    
    return all_incidents
