#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ Recursively retrieves a list of top 10 of titles of hot posts """
    global after
    user_agent = {'User-Agent': 'myRedditApp/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
