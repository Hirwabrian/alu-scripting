#!/usr/bin/python3
"""
script that Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests
def recurse(subreddit, hot_list=[], after=None):
  url = f"https://www.reddit.com/r/{subreddit}/hot.json"
  param = {'after': after, 'limit': 100}
  headers = {
    'User-Agent': 'myRedditApp/0.0.1' }
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
