import numpy as np
import scipy
import json
import spotipy
import spotipy.util as util
import pandas as pd
import csv
import re
import sys
import codecs
import spotipy
import time
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pandas.io.json import json_normalize

def track_analysis(track_id):

    segments_normalized = pd.DataFrame()
    timbre_array = []
    start = time.time()
    delta = time.time() - start
    
    features = sp.audio_analysis(track_id)
    segments = features['segments']
    segments_normalized = json_normalize(segments)
    timbre_raw = segments_normalized.iloc[:,8]

    timbre_raw_df = pd.DataFrame(timbre_raw)
    timbre_raw_df.columns = ['MFCC']

    timbre_raw_df['MFCC'] = timbre_raw_df['MFCC'].astype(str)
    timbre_raw_df['MFCC'] = timbre_raw_df['MFCC'].str.replace("[","")
    timbre_raw_df['MFCC'] = timbre_raw_df['MFCC'].str.replace("]","")

    timbre_array = timbre_raw_df.to_numpy()

    return timbre_array;

def get_tracks_from_playlist(pl_ids):
    results = sp.user_playlist(username, pl_ids)
    #print(results)
    tids = []
    #tracks = results['tracks']
    for i, t in enumerate(results['tracks']['items']):
        #print(' ', i, t['track'])
        tids.append(t['track']['id'])
    return tids;


client_id = "ef3cb42f618f4fb0a2ddc9da661f26a3"
client_secret= "ebca65d96fc34bc4b633d88e2a554a33"
redirect_uri= 'http://google.com/'
username = 'rogeriosjr'

pid = '37i9dQZF1DX49jUV2NfGku'
tid = '3mRvIW6Dr9NrSH5DazOqix'
track_list = []

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



#results = sp.search(q=artist_name, limit=50)

#tids = []
#for i, t in enumerate(results['tracks']['items']):
#    print(' ', i, t['name'])
#    tids.append(t['uri'])

track_list = get_tracks_from_playlist(pid)
print(track_list)

result = track_analysis(tid)
print(result)
print(result.shape)

