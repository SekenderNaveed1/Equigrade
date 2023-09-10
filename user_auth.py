import requests
from canvasapi import Canvas
from urllib.parse import urlencode

# Initialize parameters for OAuth2 Authentication
CLIENT_ID = 'client_id'
CLIENT_SECRET = 'client_secret'
REDIRECT_URI = 'http://example.com/callback'
base_url = 'https://ucdavis.edu'
# base_url = 'https://csulb.instructure.com' for CSULB staff and students

# Declare container for OAuth2 authorization flow with Canvas
auth_params = {
    'client_id': CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
}

# Redirect user to Canvas for authorization
authorization_url = f'{base_url}/login/oauth2/auth?{urlencode(auth_params)}'
print(f'Please visit this URL to authenticate you: {authorization_url}')

# The URL containing the authorization code will be displayed in your browsers URL
authorization_code = input('Enter the authorization code from the URL:\n')

# Exchange authorization code for an access token
token_params = {
    'grant_type': 'authorization_code',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': authorization_code,
    'redirect_uri': REDIRECT_URI,
}

# Construct token URL for exchange
token_url = f'{base_url}/login/oauth2/token'

# Make a POST request to the token URL with the token_params to exchange the authorization code.
response = requests.post(token_url, data=token_params)

OK = 200

# Check if the HTTP response status code indicates a successful request
if response.status_code == OK:
    # Extract the access token from the JSON response from the OAuth2 token endpoint
    access_token = response.json()['access_token']

    # Instantiate canvas class to interact with the API
    canvas = Canvas(base_url, access_token)

else:
    print('Error retrieving access token')



