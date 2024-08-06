import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.reddit.com/r/technology/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags with an id that starts with "post-title"
    links = soup.select('a[id^="post-title"]')

    for i, link in enumerate(links, start=1):
        print(f"{i}. {link.get_text(strip=True)} - {link['href']}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")