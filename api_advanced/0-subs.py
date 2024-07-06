#!/usr/bin/python3
"""
script that returns the number of subscribers (not active users, total subscribers) for a given subreddit
"""

import requests
def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "myRedditApp/0.0.1"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code = 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except Exception:
        return 0
