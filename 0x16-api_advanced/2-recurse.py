#!/usr/bin/python3
"recursively searches for hot topics in a subreddit"""


import requests


def recurse(subreddit, hot_list=[]):
    """recursively gets hot topics in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if res.status_code != 200:
        return None
    result = res.json()
    if len(result["data"]["children"]) == 0:
        return None
    after = result["data"]["after"]
    hot_list = rec_function(hot_list, after, url)
    return hot_list


def rec_function(hot_list, after, url):
    """recursive function"""
    if not after:
        return hot_list
    else:
        res = requests.get(url, params={"after": after},
                           headers={"User-Agent": "Mozilla/5.0"})
        result = res.json()
        new_after = result["data"]["after"]
        for child in result["data"]["children"]:
            title = child["data"]["title"]
            hot_list.append(title)
        return rec_function(hot_list, new_after, url)
