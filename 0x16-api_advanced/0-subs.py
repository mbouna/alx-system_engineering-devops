"""
subs
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'MyRedditApp/1.0 (by /u/ctbrjg1067)',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        elif response.status_code == 403:
            print("Error: Access forbidden for subreddit '{}'.".format(subreddit))
            return 0
        elif response.status_code == 404:
            print("Error: Subreddit '{}' not found.".format(subreddit))
            return 0
        else:
            print("Error: Received status code {}".format(response.status_code))
            return 0
    except requests.RequestException as e:
        print("RequestException: {}".format(e))
        return 0
