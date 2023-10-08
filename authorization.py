import requests

# Replace these with your own values
canvas_url = 'https://ucdavis.instructure.com'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'https://your-app.com/oauth/callback'  # Must match the registered callback URI

# Step 1: Redirect the user to the Canvas login and authorization page
authorization_url = f'{canvas_url}/login/oauth2/auth?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}'
# Redirect the user's browser to authorization_url

# Step 2: Handle the callback with the authorization code
# Extract the authorization code from the callback URL

# Step 3: Exchange the authorization code for an access token
token_url = f'{canvas_url}/login/oauth2/token'
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'code': authorization_code,
    'redirect_uri': redirect_uri,
    'grant_type': 'authorization_code'
}
response = requests.post(token_url, data=data)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    # Now you can use the access_token to make authenticated API requests
else:
    print(f'Error exchanging code for access token: {response.status_code}')
