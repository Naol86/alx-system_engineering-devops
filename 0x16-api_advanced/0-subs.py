#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API to get the number of subscribers for a subreddit."""
    headers = {
        "User-Agent": "0x16. API_advanced-e_kiminza using python-requests"
    }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    except (ValueError, AttributeError, KeyError):
        return 0
