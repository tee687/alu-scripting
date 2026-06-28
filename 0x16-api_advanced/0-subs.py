# Write the clean code directly into that new path
cat << 'EOF' > /alu-scripting/0x16-api_advanced/0-subs.py
#!/usr/bin/python3
"""
Module for querying the Reddit API and returning the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the total subscribers for a subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Ubuntu14.04:API.Advanced:v1.0.0 (by /u/student)"
    }
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
        
    try:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        return 0
