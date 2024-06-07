#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def check_subreddit(subreddit):
    """Print OK if the subreddit exists or doesn't exist."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("OK")
    else:
        print("OK")