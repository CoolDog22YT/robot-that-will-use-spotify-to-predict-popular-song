import os
# import necessary libraries
import os
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytrends.request import TrendReq

# define Spotify client ID and client secret
SPOTIFY_CLIENT_ID = os.environ['Spotify client id']
SPOTIFY_CLIENT_SECRET = os.environ['Spotify client secret']

# set up Spotify API client with client credentials
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# set up PyTrends client
pytrends = TrendReq()

# search for current top song on Spotify
top_track = sp.playlist_tracks('37i9dQZEVXbMDoHDwVN2tF')['items'][0]['track']['name']

# build PyTrends request for related queries
pytrends.build_payload(kw_list=[top_track], timeframe='today 1-m', geo='US')
time.sleep(2)
related_queries = pytrends.related_queries()

# get the top related query for the top song
top_related_query = related_queries[top_track]['top'].iloc[0]['query']

# search for top result in Spotify
results = sp.search(q=top_related_query, type='track', limit=1)

# get the top song from the search results
top_song = results['tracks']['items'][0]['name']

# print the predicted next popular song
print(f"The next popular song will be: {top_song}")
