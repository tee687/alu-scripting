#!/usr/bin/python3
"""
Module for recursively querying the Reddit API to fetch all hot articles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. Returns None if invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {"after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        after = data.get("after")
        children = data.get("children", [])

        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
