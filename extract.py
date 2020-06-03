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
    timbre_split = pd.DataFrame(columns=['A','B','C','D','E','F','G','H','I','J','K','L'])
    timbre_array = pd.DataFrame()
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

    timbre_split = timbre_raw_df['MFCC'].str.split(',',expand=True)

    timbre_array = timbre_split.astype(float)

    return timbre_array;
    #return timbre_split;

def get_tracks_from_playlist(pl_ids):
    results = sp.user_playlist(username, pl_ids)
    #print(results)
    tids = []
    #tracks = results['tracks']
    for i, t in enumerate(results['tracks']['items']):
        #print(' ', i, t['track'])
        tids.append(t['track']['id'])
    return tids;

#def track_pre_processing(track_res):

client_id = ""
client_secret= ""
redirect_uri= 'http://google.com/'
username = ''

#pid = '37i9dQZF1DX49jUV2NfGku'

#test_extract 
pid = '4RJt50gxyrztWYSE3qvsdy'
tid = '3mRvIW6Dr9NrSH5DazOqix'  
track_list = []

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

track_list = get_tracks_from_playlist(pid)
print(track_list)

#result_raw = []
result_raw = pd.DataFrame()

for i, val in enumerate(track_list):
    res = track_analysis(track_list[i])
    #print(res)
    result_raw = result_raw.append(res)

#result_raw = track_analysis(tid)
print(result_raw)
print(result_raw.shape)

#export_csv = result_raw.to_csv(r'C:\Users\I840615\Documents\Dev\test.csv', index = None, header=True)
