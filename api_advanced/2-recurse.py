#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}
    
    headers = {
        'User-Agent': 'myRedditApp/0.0.1'
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            for post in posts:
                hot_list.append(post['data']['title'])
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as error:
        return None
