#!/usr/bin/python3
"""
A simple function to get the number of subscribers of a subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """A function to start sending requests to the API."""
    client_id = "vCoCeS5JDM_uX__qWq9dLA"
    secret = "Xv4PSvskDSyCA_O0tLULNOjr53fQcg"
    auth = requests.auth.HTTPBasicAuth(client_id, secret)
    data = {
        'grant_type': 'password',
        'username': 'Majestic_Bluebird490',
        'password': "0633barcelone@M"
    }
    headers = {'User-Agent': 'MyAPI'}
    res = requests.post("https://www.reddit.com/api/v1/access_token",
                        auth=auth, data=data, headers=headers)

    token = res.json()['access_token']
    headers['Authorization'] = 'bearer {}'.format(token)

    response = requests.get('https://oauth.reddit.com/r/{}/about'.format(subreddit), headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
