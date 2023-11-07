#!/usr/bin/python3
"""Prints the titles of the first 10
hot posts for a given subreddit"""


def top_ten(subreddit):
    """Titles for the top ten
    subreddits
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 