#!/usr/bin/python3
"""
This module contains a function that recursively queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.

The function handles pagination using recursion and includes error handling for invalid subreddits.

Functions:
    recurse(subreddit, hot_list=[], after=None): Recursively fetches titles of hot articles for a subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the hot article titles.
        after (str): The pagination token to fetch the next set of results.

    Returns:
        list: A list of titles of hot articles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}
    
    headers = {
        'User-Agent': 'myRedditApp/0.0.1'  # Custom User-Agent to identify the client
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            # Append the titles of the hot posts to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # If there is a next page, recursively call the function
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
