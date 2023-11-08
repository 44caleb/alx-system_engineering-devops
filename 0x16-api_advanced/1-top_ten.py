#!/usr/bin/python3
"""requests subscriber data from reddit api"""


import requests


def top_ten(subreddit):
    """prints titles of first 10 hit posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    res = requests.get(url, params=params, headers={'User-Agent': 'Mozilla/5.0'})
    if res.status_code != 200:
        print(None)
    else:
        result = res.json()
        if len(result["data"]["children"]) == 0:
            print(None)
            return
        for child in result["data"]["children"]:
            print(child["data"]["title"])
