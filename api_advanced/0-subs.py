#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"  
    headers = {"User-Agent": "Hbrian"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers  
        else:
            return None  
    
    except Exception as error:
        print(f"An error occurred: {error}")
        return None
