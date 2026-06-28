#!/usr/bin/python3
"""
Module for querying the Reddit API and printing titles of the top 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Ubuntu14.04:API.Advanced:v1.0.0 (by /u/student)"
    }
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        
        if not children:
            print(None)
            return

        for post in children:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
