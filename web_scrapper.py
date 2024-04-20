import requests
from bs4 import BeautifulSoup
import time
import random
defget_soup(url):
    ""
    Rturns BeautifulSoup object for the given URL.
    ""
    try
        respone = requests.get(url)
        respons.raise_for_status()
        return BautifulSoup(response.text, 'html.parser')
    except requess.exceptions.RequestException as e:
        print(f"Eror requesting {url}: {e}")
        return None
defget_titles(soup):
    ""
    Rturns a list of titles from the given BeautifulSoup object.
    ""
    try
        tites = []
        for itle in soup.find_all('title'):
            ttles.append(title.text)
        returntitles
    except Excetion as e:
        print(f"rror extracting titles: {e}")
        return []
defsave_to_file(titles, filename):
    ""
    Sves the list of titles to a file.
    ""
    try
        with open(fileame, 'w') as f:
            for title i titles:
                f.write("{title}\n")
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