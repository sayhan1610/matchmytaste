from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI app 
app = FastAPI()
 
# CORS (Cross-Origin Resource Sharing) middleware configuration 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, modify this based on your requirements
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Spotify credentials 
SPOTIPY_CLIENT_ID = os.getenv('spoti_id')
SPOTIPY_CLIENT_SECRET = os.getenv('spoti_token')

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
    # Search for the initial artist
    results = sp.search(q=search_input.query, type='artist', limit=1)
    artists = results['artists']['items']
    if artists:
        artist_id = artists[0]['id']
        related_artists = sp.artist_related_artists(artist_id)['artists'][:20]  # Limit to 20 related artists
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
        recommended_tracks = sp.recommendations(seed_tracks=[track_id], limit=50)['tracks']
        return [{'name': track['name'], 'artists': ', '.join([artist['name'] for artist in track['artists']]), 'url': track['external_urls']['spotify']} for track in recommended_tracks]
    else:
        raise HTTPException(status_code=404, detail=f"No tracks found for '{search_input.query}'.")

@app.get("/top_tracks_of_month", response_model=list[Track])
def top_tracks_of_month():
    # Get current month and year
    today = datetime.date.today()
    year = today.year
    month = today.month

    # Fetch top tracks of the month
    results = sp.search(q=f'year:{year} month:{month}', type='track', limit=50)
    top_tracks = results['tracks']['items']
    return [{'name': track['name'], 'artists': ', '.join([artist['name'] for artist in track['artists']]), 'url': track['external_urls']['spotify']} for track in top_tracks]

@app.get("/")
def ping():
    return "pong"

if __name__ == "__main__":
    import uvicorn

    # Get port number from environment variable PORT, defaulting to 8000 if not set
    port = int(os.getenv("PORT", 8000))
    
    # Run the FastAPI application using Uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
