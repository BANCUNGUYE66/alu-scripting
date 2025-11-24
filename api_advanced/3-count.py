#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    """
    if not word_list or word_list == [] or not subreddit:
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu-scripting:v1.0.0 (by /u/BANCUNGUYE66)"
    }
    params = {
        "limit": 100,
        "after": after
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        results = response.json().get("data")
        after = results.get("after")
        children = results.get("children")

        # Initialize counts dictionary on first call
        if not counts:
            for word in word_list:
                counts[word.lower()] = 0

        for child in children:
            title = child.get("data").get("title").lower().split()
            for word in word_list:
                word_lower = word.lower()
                # Count occurrences of the word in the title
                counts[word_lower] += title.count(word_lower)

        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            # Sort results: Descending by count, then Ascending alphabetically
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word, count))

    except Exception:
        return None
