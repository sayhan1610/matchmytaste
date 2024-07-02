from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

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
    # Search for artists based on query
    results = sp.search(q=search_input.query, type='artist', limit=50)  # Increased limit to 50
    artists = results['artists']['items']
    
    if artists:
        related_artists_list = []
        
        # Iterate over each artist found
        for artist in artists:
            artist_id = artist['id']
            related_artists = sp.artist_related_artists(artist_id)['artists']
            
            # Append related artists to the list
            for related_artist in related_artists:
                related_artists_list.append({
                    'name': related_artist['name'],
                    'url': related_artist['external_urls']['spotify']
                })
        
        return related_artists_list
    
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

@app.get("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    import uvicorn

    # Get port number from environment variable PORT, defaulting to 8000 if not set
    port = int(os.getenv("PORT", 8000))
    
    # Run the FastAPI application using Uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
