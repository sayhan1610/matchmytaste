from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime

# Spotify credentials
SPOTIPY_CLIENT_ID = 'e1212180fa8d43bdac68a2e39697350b'
SPOTIPY_CLIENT_SECRET = 'ajifbfao'

# Initialize FastAPI app
app = FastAPI()

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

class SearchInput(BaseModel):
    query: str

class Artist(BaseModel):
    name: str
    url: str

class Track(BaseModel):
    name: str
    artists: str
    url: str

@app.post("/search_artist", response_model=list[Artist])
def search_artist(search_input: SearchInput):
    # Search for similar artists
    results = sp.search(q=search_input.query, type='artist', limit=1)
    artists = results['artists']['items']
    if artists:
        artist_id = artists[0]['id']
        related_artists = sp.artist_related_artists(artist_id)['artists']
        return [{'name': artist['name'], 'url': artist['external_urls']['spotify']} for artist in related_artists]
    else:
        raise HTTPException(status_code=404, detail=f"No artists found for '{search_input.query}'.")

@app.post("/search_track", response_model=list[Track])
def search_track(search_input: SearchInput):
    # Search for similar tracks
    results = sp.search(q=search_input.query, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        track_id = tracks[0]['id']
        recommended_tracks = sp.recommendations(seed_tracks=[track_id], limit=10)['tracks']
        return [{'name': track['name'], 'artists': ', '.join([artist['name'] for artist in track['artists']]), 'url': track['external_urls']['spotify']} for track in recommended_tracks]
    else:
        raise HTTPException(status_code=404, detail=f"No tracks found for '{search_input.query}'.")

@app.get("/top_tracks_of_month", response_model=list[Track])
def top_tracks_of_month():
    # Get current month and year
    today = datetime.date.today()
    year = today.year
    month = today.month

    # Get first and last day of the current month
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

    # Format dates for Spotify API
    start_date = first_day.strftime('%Y-%m-%d')
    end_date = last_day.strftime('%Y-%m-%d')

    # Fetch top tracks of the month
    results = sp.search(q=f'year:{year} month:{month}', type='track', limit=10)
    top_tracks = results['tracks']['items']
    return [{'name': track['name'], 'artists': ', '.join([artist['name'] for artist in track['artists']]), 'url': track['external_urls']['spotify']} for track in top_tracks]

