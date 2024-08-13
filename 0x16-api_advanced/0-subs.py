#!/usr/bin/python3
"""script for parsing web data from an api
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """api call to reddit to get the number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'
    headers = {
        'User-Agent': 'My-User-Agent'}
    # grab info about all users
    url = base_url + '{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)

    try:
        # grab the info about the users' tasks
        data = resp.get('data')
        subscribers = data.get('subscribers')
    except:
        return 0
    if subscribers is None:
        return 0
    return int(subscribers)
