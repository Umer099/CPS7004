import requests
from bs4 import BeautifulSoup
import time

# URL of the Reddit technology page
url = 'https://www.reddit.com/r/technology/'

#add delay of 1 sec
time.sleep(1)

#send a GET request to the website
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    #Find all <shreddit-post'>

    posts = soup.select('shreddit-post')

    for post in posts:
        print(f"""
        Title: {post['post-title']}
        Author: {post['author']}
        posted: {post['created-timestamp']}
        stats: Score =  {post['score']}, Comments = {post['comment-count']}
        Permalink: {post['permalink']}
        
        
        
        
        
       """ )
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")