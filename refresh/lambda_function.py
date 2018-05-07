import requests


# requires: refresh_token
def lambda_handler(event, context):
    required = ['refresh_token']
    for param in required:
        if param not in event:
            return 'Error: missing parameter: %s' % param
    r = requests.post('https://accounts.spotify.com/api/token', data={
       'grant_type': 'refresh_token',
       'refresh_token': event['refresh_token'],
    }, headers={
        'Authorization': 'Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    })
    return r.text
