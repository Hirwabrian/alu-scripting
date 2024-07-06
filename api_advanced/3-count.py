#!/usr/bin/python3
"""Module for task 3"""

import requests


def count_words(subreddit, word_list, after="", word_count={}):
    """count all words"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/0.0.1"}
    params = {'after': after, 'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            return
        
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']
        
        # Normalize the word list to lowercase
        normalized_word_list = [word.lower() for word in word_list]
        
        for post in posts:
            # Normalize the title and split into words
            title = post['data']['title'].lower().split()
            for word in title:
                # Clean the word to remove non-alphabetic characters
                cleaned_word = ''.join(filter(str.isalpha, word)) 
                if cleaned_word in normalized_word_list:
                    if cleaned_word in word_count:
                        word_count[cleaned_word] += 1
                    else:
                        word_count[cleaned_word] = 1
        
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            if word_count:
                # Sort the word counts by count (descending) and then alphabetically
                sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_words:
                    print(f"{word}: {count}")
    
    except Exception as error:
        print(f"An error occurred: {error}")
