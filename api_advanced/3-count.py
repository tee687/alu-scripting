#!/usr/bin/python3
"""
Module for recursively querying the Reddit API and counting word occurrences.
"""
import requests


def count_words(subreddit, word_list, instances={}, after=None):
    """
    Recursively queries the Reddit API, parses titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    # Initialize dictionary on the first recursive call
    if not instances:
        for word in word_list:
            instances[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {"after": after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        after = data.get("after")
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            # Split title strictly by spaces to extract pure words
            words = title.split()
            for word in words:
                if word in instances:
                    instances[word] += 1

        # If there's another page, recurse
        if after is not None:
            return count_words(subreddit, word_list, instances, after)

        # Base case: no more pages. Sort and print results.
        # Filter out words with 0 counts
        filtered_counts = {k: v for k, v in instances.items() if v > 0}
        if not filtered_counts:
            return

        # Sort primarily by count descending (-x[1]), then alphabetically (x[0])
        sorted_words = sorted(filtered_counts.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_words:
            print("{}: {}".format(word, count))

    except Exception:
        return
