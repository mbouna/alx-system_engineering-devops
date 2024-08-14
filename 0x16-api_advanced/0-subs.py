
import requests

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


def number_of_subscribers(subreddit):
    """ a function to startsending requests to API"""
    resp = requests.get('https://oauth.reddit.com/r/{}/about'
                        .format(subreddit), headers=headers)

    if (resp.status_code != 200):
        return 0

    try:
        json_resp = resp.json()

    except ValueError:
        return 0

    data = json_resp.get('data')

    if data:
        subs = data.get('subscribers')
        if subs:
            return subs

    return 0
