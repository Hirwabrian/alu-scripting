#!/usr/bin/python3
"""Script that queries the Reddit API"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Hbrian"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"][:10]
            
            for post in posts:
                print(post["data"]["title"])
        
        else:
            print("None")
    
    except requests.RequestException as error:
        print(f"Error fetching data: {error}")
        print("None")
