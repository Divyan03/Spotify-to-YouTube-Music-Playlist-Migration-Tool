from dotenv import load_dotenv
import os
import json 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

cid = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")
playlist_id = "3fadDkRiUueKuMeYCLJvIm"

# def connect(cl_id,cl_secret):
#     sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))
#     return sp

def fetch_playlist_by_id(api, id):
    playlist_res = api.playlist(playlist_id=id)
    name = playlist_res['name']
    playlist_items = playlist_res['tracks']['items']
    return playlist_items, name

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = cid, client_secret = secret))

playlist_items = fetch_playlist_by_id(sp, playlist_id)
print(json.dumps(playlist_items)) 