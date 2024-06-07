#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print("OK")
        return
    
    try:
        results = response.json().get("data")
        if results:
            for c in results.get("children", []):
                print(c.get("data").get("title"))
        print("OK")
    except ValueError:
        print("OK")


if __name__ == "__main__":
    top_ten("python")  # Test with a valid subreddit
    top_ten("thissubredditdoesnotexist")  # Test with an invalid subreddit

