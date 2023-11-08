#!/usr/bin/python3
"""requests subscriber data from reddit api"""


import requests



def number_of_subscribers(subreddit):
    """returns number of subscribers in a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        return 0
    data = response.json()
    subscribers = data["data"]["subscribers"]
    return subscribers
