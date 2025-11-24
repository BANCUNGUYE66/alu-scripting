#!/usr/bin/python3
"""
Recursive function to query the Reddit API and return a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
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

        for child in children:
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except Exception:
        return None
