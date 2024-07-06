#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "myRedditApp/0.0.1"}
    try:
        result = requests.get(url, headers=headers, allow_redirects=False)
        
        if result.status_code == 404:
            print("None")
            return

        result = result.json()
        posts = result["data"]["children"][:10]
        
        for post in posts:
            print(post["data"]["title"])
    
    except Exception as error:
        print("None")
