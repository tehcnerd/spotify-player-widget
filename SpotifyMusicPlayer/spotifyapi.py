import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import getname
client_id = "your-client-id"
client_secret = "your-client-secret"

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_album_art():
    if getname.get_spotify_title() == "NAN - Play a Song":
        image_url = "https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/music-audio/vinyl-record-ez5xvbsxj5w1h1d8r0c8ta.png/vinyl-record-o3qnrd2huan26xx2mjzr.png?_a=DAJFJtWIZAAC"
    else:   
            query = getname.get_spotify_title()
            results = sp.search(q=query, type='track', limit=1)

            if results['tracks']['items']:
                track = results['tracks']['items'][0]
                album = track['album']
                image_url = album['images'][0]['url']
    return image_url
