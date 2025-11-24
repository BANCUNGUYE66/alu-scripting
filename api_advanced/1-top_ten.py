#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # CHANGE: Using a unique User-Agent with your username to bypass blocks
    headers = {
        "User-Agent": "python:alu-scripting:v1.0.0 (by /u/BANCUNGUYE66)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        # If the status code is not 200 (OK), the subreddit is invalid
        if response.status_code != 200:
            print("None")
            return

        results = response.json().get("data")
        children = results.get("children")

        # Print the titles
        for child in children:
            print(child.get("data").get("title"))

    except Exception:
        print("None")
