#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit (without '/r/').

    Returns:
    - None: Prints the titles of the top 10 posts.
            If the subreddit doesn't exist or there's an error, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "myRedditApp/0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            print(post['data']['title'])

    except Exception as error:
        print(None)
