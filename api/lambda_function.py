import requests


# requires: endpoint, auth code
def lambda_handler(event, context):
    required = ['auth', 'endpoint']
    for param in required:
        if param not in event:
            return 'Error: missing parameter: %s' % param
    r = requests.get("https://api.spotify.com/" + event['endpoint'], headers={'Authorization': 'Bearer ' + event['auth']})
    return r.text
