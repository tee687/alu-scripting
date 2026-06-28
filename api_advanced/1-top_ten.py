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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            for post in children:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
