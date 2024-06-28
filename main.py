# from credentials import my_client_secret, my_client_id,yt_api
from spotify_api import connect,fetch_playlist_by_id,extract_data,query_builder
from ytOauth import makePlaylist, addItemToPlaylist, makeService
from ytapi import getVideoIds
import os

from dotenv import load_dotenv
load_dotenv()

cid = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")
playlist_id = os.getenv("PLAYLIST")
ytKey = os.getenv("YOUTUBE_KEY")

def main(playlist):
    api = connect(cid,secret)
    items_name = fetch_playlist_by_id(api,playlist)
    name = items_name[1]
    queries = query_builder(extract_data(api,items_name[0]))
    videoIds = getVideoIds(queries,ytKey)
   
    service = makeService()
    new_play_id = makePlaylist(service,name)
    addItemToPlaylist(service,new_play_id,videoIds)
    print("finished migrating")
    # return queries
    return new_play_id

main(playlist_id)