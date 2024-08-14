import requests

subreddit = argv[1]
def set_config_params():
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
    print("Response status code:", res.status_code)
    print("Response JSON:", res.json())
    if res.status_code == 200 and 'access_token' in res.json():
        token = res.json()['access_token']
        headers['Authorization'] = 'bearer {}'.format(token)
        return headers
    else:
        raise Exception("Failed to obtain access token. Response: {}".format(res.json()))

def number_of_subscribers(subreddit):
    """A function to start sending requests to API."""
    headers = set_config_params()
    test = requests.get('https://oauth.reddit.com/r/{}/about'.format(subreddit), headers=headers)
    if test.status_code == 200:
        return test.json()["data"]["subscribers"]
    else:
        return 0
