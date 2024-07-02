# SongThisDay API

## Overview

SongThisDay API is a web service built with FastAPI to retrieve information about music artists and tracks. It interacts with the Spotify API to search for similar artists, similar tracks, and fetch the top tracks of the month based on user queries.

## Endpoints

### Search for Similar Artists

- **Endpoint**: `/search_artist`
- **Method**: POST
- **Description**: Returns a list of similar artists based on the provided artist name or query.
- **Input**: JSON body `{ "query": "artist_name" }`
- **Output**: List of artists with their names and Spotify URLs.

### Search for Similar Tracks

- **Endpoint**: `/search_track`
- **Method**: POST
- **Description**: Returns a list of similar tracks based on the provided track name or query.
- **Input**: JSON body `{ "query": "track_name" }`
- **Output**: List of tracks with their names, artists, and Spotify URLs.

### Fetch Top Tracks of the Month

- **Endpoint**: `/top_tracks_of_month`
- **Method**: GET
- **Description**: Fetches the top tracks of the current month based on Spotify's popularity metrics.
- **Output**: List of tracks with their names, artists, and Spotify URLs.

## Getting Started

1. Clone the repository.
2. Install dependencies from `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Spotify API credentials in the environment variables (SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET).
4. Run the FastAPI application using Uvicorn.
   uvicorn main:app --reload
