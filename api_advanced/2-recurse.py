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
    # Construct the URL for the Reddit API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Parameters for the request: after is used for pagination, limit is set to 100
    params = {'after': after, 'limit': 100}
    
    # Headers to identify the user-agent making the request
    headers = {
        'User-Agent': 'myRedditApp/0.0.1'
    }

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON data
            data = response.json()
            # Extract the list of posts
            posts = data['data']['children']
            # Get the token for the next page of results
            after = data['data']['after']

            # Append the title of each post to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])
            # If there are more pages, recursively call the function with the new 'after' token
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the list of post titles
                return hot_list
        else:
            # Request failed, return None
            return None
    except Exception as error:
        # Handle exceptions (e.g., network issues) and return None
        return None
