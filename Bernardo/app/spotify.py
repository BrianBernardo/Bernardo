# app/spotify.py
import requests
import base64

# Spotify API credentials
CLIENT_ID = 'd76da70aeb3e46b08aeac9609c8fa56c'
CLIENT_SECRET = 'c1dc69ea20e54d06bfe65e6c852abb4d'

# Get access token from Spotify API
def get_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode('utf-8')

    headers = {
        'Authorization': f'Basic {auth_header}',
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(auth_url, headers=headers, data=data)
    response_data = response.json()

    return response_data['access_token']

# Get playlists by mood from Spotify
def get_playlist_by_mood(mood):
    token = get_access_token()
    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'q': mood,  # Query parameter for mood
        'type': 'playlist',
        'limit': 20  # Number of playlists to return
    }

    response = requests.get(search_url, headers=headers, params=params)
    response_data = response.json()

    # Extract playlist info from response
    playlists = [
        {
            'name': playlist['name'],
            'url': playlist['external_urls']['spotify'],
            'image': playlist['images'][0]['url'] if playlist['images'] else None
        }
        for playlist in response_data['playlists']['items']
    ]

    return playlists
