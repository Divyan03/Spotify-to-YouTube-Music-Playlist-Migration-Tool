import os
import json 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def connect(cl_id,cl_secret):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(cl_id, cl_secret))
    return sp

def fetch_playlist_by_id(api, id):
    playlist_res = api.playlist(playlist_id=id)
    name = playlist_res['name']
    playlist_items = playlist_res['tracks']['items']
    return playlist_items, name


def extract_data(api, items):
    data = []
    for i in items:
        item = dict.fromkeys(['track_name','artist_name','album_name'])
        track_name = i['track']['name']
        artist_name = i['track']['artists'][0]['name']
        album_name = i['track']['album']['name']

        item['track_name'] = track_name
        item['artist_name']= artist_name
        item['album_name']= album_name

        data.append(item)
        # print(item)
    return data

def query_builder(pl_data):
    queries = []
    for obj in pl_data:
        q = "{} {} {}".format(obj['track_name'],obj['album_name'],obj['artist_name'])
        queries.append(q)
    return queries



# api = connect(cid,secret)
# pl = fetch_playlist_by_id(api,playlist_id)
# print(pl)

# print("\n")
# print(query_builder(extract_data(api,pl[0])))