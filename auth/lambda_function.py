import requests


# requires: code
def lambda_handler(event, context):
    required = ['code']
    for param in required:
        if param not in event:
            return 'Error: missing parameter: %s' % param
    r = requests.post('https://accounts.spotify.com/api/token', data={
       'grant_type': 'authorization_code',
       'code': event['code'],
       'redirect_uri': 'https://ehennenfent.github.io/spotify-analytics/',
       'client_id': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
       'client_secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    })
    return r.text
