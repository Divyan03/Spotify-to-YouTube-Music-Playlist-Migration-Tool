from googleapiclient.discovery import build
# from credentials import yt_api
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

ytKey = os.getenv('YOUTUBE_KEY')

def makePublicService(api_key):
    service = build(serviceName='youtube',version='v3',developerKey=api_key)
    return service

def getVideoIds(queries,api):
    service = makePublicService(api)
    ids = []
    for i in range(len(queries)):
        request = service.search().list(part="snippet",
                maxResults=2,
                q = queries[i]
            )
        response = request.execute()
        videoid = response['items'][0]['id']['videoId']
        print(videoid)

        ids.append(videoid)
        time.sleep(3)
    return ids

# print(getVideoIds(['Devil In A New Dress My Beautiful Dark Twisted Fantasy Kanye West', '90210 (feat. Kacy Hill) Rodeo Travis Scott'], ytKey))