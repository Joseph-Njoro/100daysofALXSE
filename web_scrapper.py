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

def get_usernames(soup):
    """
    Returns a list of usernames from the given BeautifulSoup object.
    """
    try:
        usernames = []
        # Modify this part to find usernames on the webpage
        # For example, if the usernames are found in <a> tags with class="username", you can use:
        for link in soup.find_all('a', class_='username'):
            usernames.append(link.text.strip())
        return usernames
    except Exception as e:
        print(f"Error extracting usernames: {e}")
        return []

def save_to_file(usernames, filename):
    """
    Saves the list of usernames to a file.
    """
    try:
        with open(filename, 'w') as f:
            for username in usernames:
                f.write(f"{username}\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    """
    The main function that scrapes the websites and saves the usernames to a file.
    """
    # Prompt user to enter a username or email
    search_query = input("Enter a username or email to search for: ")

    urls = [
        'https://www.instagram.com',
        'https://www.facebook.com',
        'https://www.tiktok.com',
        'https://www.snapchat.com',
        'https://www.twitter.com',
        'https://www.linkedin.com',
        'https://www.reddit.com',
        'https://www.pinterest.com',
        # Add more URLs as needed
    ]

    for url in urls:
        print(f"Scraping {url}...")
        soup = get_soup(url)
        if soup:
            usernames = get_usernames(soup)
            if usernames:
                save_to_file(usernames, 'usernames.txt')
                print(f"Saved {len(usernames)} usernames to usernames.txt")
            else:
                print("No usernames found")
        else:
            print("Failed to scrape website")

        # Add a random delay to avoid overwhelming the websites
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    main()