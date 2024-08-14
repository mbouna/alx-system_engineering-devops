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
token = res.json().get('access_token')
headers['Authorization'] = 'bearer {}'.format(token)


def top_ten(subreddit):
    """ a function to start sending requests to API"""
    test = requests.get('https://oauth.reddit.com/r/{}/hot'
                        .format(subreddit), headers=headers)
    if test.status_code == 200:
        try:
            json_data = test.json()
            res = []
            for post in json_data["data"]["children"]:
                res.append(post["data"]["title"])
            for i in range(10):
                print(res[i])
        except ValueError:
            print("Error: Response is not valid JSON")
            return 0
    else:
        print("Error: Status code is not 200")
        return 0
