#!/usr/bin/python3
"""Total number of subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """Total number of subs
    Args:
        subreddit - String
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    result = response.json()
    try:
        return result['data']['subscribers']

    except Exception:
        return 0
