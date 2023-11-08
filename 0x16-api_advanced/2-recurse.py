#!/usr/bin/python3
"""recursively gets hot topics in a subreddit"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    sub = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=user_agent)

    try:
        sub = sub.json().get('data')
        after = sub.get('after')
        sub = sub.get('children')
        for obj in sub:
            hot_list.append(obj['data'].get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except:
        return(None)
