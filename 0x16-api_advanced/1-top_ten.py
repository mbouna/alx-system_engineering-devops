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


def top_ten(subreddit):
    """ a function to startsending requests to API"""
    test = requests.get('https://oauth.reddit.com/r/{}/hot'
                        .format(subreddit), headers=headers)
    if test.status_code == 200:
        res = []
        for post in test.json()["data"]["children"]:
            res.append(post["data"]["title"])
        for i in range(10):
            print(res[i])
    else:
        print(None)
