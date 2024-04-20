import requests
from bs4 import BeautifulSoup
import time
import random

def get_soup(url):
    """
    Returns BeautifulSoup object for the given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return None

def get_titles(soup):
    """
    Returns a list of titles from the given BeautifulSoup object.
    """
    try:
        titles = []
        for title in soup.find_all('title'):
            titles.append(title.text)
        return titles
    except Exception as e:
        print(f"Error extracting titles: {e}")
        return []

def save_to_file(titles, filename):
    """
    Saves the list of titles to a file.
    """
    try:
        with open(filename, 'w') as f:
            for title in titles:
                f.write(f"{title}\n")
    except Exception as e
        print(f"Error saving to file: {e}")
defmain():
    ""
    Te main function that scrapes the websites and saves the titles to a file.
    ""
    urls = 
        'https://www.example1.com',        'https://www.example2.com',
    'https://www.example3.com',
       # Add more URLs as needed
    ]
    for url n urls:
        printf"Scraping {url}...")
        soup =get_soup(url)
        if soup
            titles = et_titles(soup)
            if titles:                save_to_file(titles, 'titles.txt')
            print(f"Saved {len(titles)} titles to titles.txt")
        else:
            print("No titles found")
        else
            print("Failed to scrape website")
        # Add a random delay to avoid oerwhelming the websites
        time.sleep(random.uniform(1, 3))
if __nam__ == "__main__":
    main(