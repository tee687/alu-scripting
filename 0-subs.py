#!/usr/bin/python3
"""
Module for querying the Reddit API recursively and sorting results.
"""
import requests
import sys


def fetch_posts_recursive(subreddit, after=None, accumulated_posts=None):
    """
    Recursively queries the Reddit API to fetch all hot posts.
    """
    if accumulated_posts is None:
        accumulated_posts = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Ubuntu14.04:AdvancedAPI.Project:v1.0.0 (by /u/student)"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data_payload = response.json().get("data", {})
    children = data_payload.get("children", [])
    next_after = data_payload.get("after", None)

    for post in children:
        post_data = post.get("data", {})
        accumulated_posts.append({
            "title": post_data.get("title"),
            "score": post_data.get("score", 0)
        })

    if next_after is None:
        return accumulated_posts
    else:
        return fetch_posts_recursive(subreddit, next_after, accumulated_posts)


def main():
    """
    Main entry point for execution.
    """
    if len(sys.argv) < 2:
        print("Usage: ./0-subs.py <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    raw_results = fetch_posts_recursive(subreddit)

    if raw_results is None:
        print("OK")
        sys.exit(0)

    sorted_posts = sorted(raw_results, key=lambda x: x["score"], reverse=True)

    for post in sorted_posts[:5]:
        print("[{}] {}".format(post["score"], post["title"]))


if __name__ == "__main__":
    main()
