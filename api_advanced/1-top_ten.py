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
    headers = {
        "User-Agent": "linux:0x01.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        results = response.json().get("data")
        children = results.get("children")

        for child in children:
            print(child.get("data").get("title"))

    except Exception:
        print("None")
