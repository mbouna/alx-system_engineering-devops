#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = headers = {'User-Agent': 'My-User-Agent'}
    with requests.session() as client:
        info = client.get(url, headers=headers, allow_redirects=False).json()
        try:
            return info.get('data', {}).get('subscribers', 0)
        except Exception:
            return 0
