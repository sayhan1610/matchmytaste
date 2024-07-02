# SongThisDay API

## Overview

SongThisDay API is a web service built with FastAPI to retrieve information about music artists and tracks. It interacts with the Spotify API to search for similar artists, similar tracks, and fetch the top tracks of the month based on user queries.

## Accessing the API

You can use the SongThisDay API in two ways: directly from the provided URL or by setting it up locally.

### 1. Use the Existing API

The API is hosted and can be accessed from [https://matchmytaste.onrender.com/](https://matchmytaste.onrender.com/).

#### Endpoints

##### Ping

- **Endpoint**: `/ping`
- **Method**: GET
- **Description**: Returns "pong" to check if the API is running.

##### Search for Similar Artists

- **Endpoint**: `/search_artist`
- **Method**: POST
- **Description**: Returns a list of similar artists based on the provided artist name or query.
- **Input**: JSON body `{ "query": "artist_name" }`
- **Output**: List of artists with their names and Spotify URLs.

##### Search for Similar Tracks

- **Endpoint**: `/search_track`
- **Method**: POST
- **Description**: Returns a list of similar tracks based on the provided track name or query.
- **Input**: JSON body `{ "query": "track_name" }`
- **Output**: List of tracks with their names, artists, and Spotify URLs.

##### Fetch Top Tracks of the Month

- **Endpoint**: `/top_tracks_of_month`
- **Method**: GET
- **Description**: Fetches the top tracks of the current month based on Spotify's popularity metrics.
- **Output**: List of tracks with their names, artists, and Spotify URLs.

### Example Requests

#### Ping

```bash
curl -X GET "https://matchmytaste.onrender.com/ping"
```

#### Search for Similar Artists

```bash
curl -X POST "https://matchmytaste.onrender.com/search_artist" -H "Content-Type: application/json" -d '{"query": "artist_name"}'
```

#### Search for Similar Tracks

```bash
curl -X POST "https://matchmytaste.onrender.com/search_track" -H "Content-Type: application/json" -d '{"query": "track_name"}'
```

#### Fetch Top Tracks of the Month

```bash
curl -X GET "https://matchmytaste.onrender.com/top_tracks_of_month"
```

### 2. Use it Locally

Follow these steps to set up and run the API on your local machine.

#### Prerequisites

- Python 3.7+
- Spotify API credentials (Client ID and Client Secret)

#### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/songthisday-api.git
   cd songthisday-api
   ```

2. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Spotify API credentials in the environment variables:

   ```bash
   export SPOTIPY_CLIENT_ID='your_spotify_client_id'
   export SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
   ```

4. Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

#### Local Endpoints

The endpoints are the same as those listed above but will be accessed at `http://127.0.0.1:8000`.

### Example Requests

#### Ping

```bash
curl -X GET "http://127.0.0.1:8000/ping"
```

#### Search for Similar Artists

```bash
curl -X POST "http://127.0.0.1:8000/search_artist" -H "Content-Type: application/json" -d '{"query": "artist_name"}'
```

#### Search for Similar Tracks

```bash
curl -X POST "http://127.0.0.1:8000/search_track" -H "Content-Type: application/json" -d '{"query": "track_name"}'
```

#### Fetch Top Tracks of the Month

```bash
curl -X GET "http://127.0.0.1:8000/top_tracks_of_month"
```

### Error Handling

- **400 Bad Request**: Returned if the input query is missing or malformed.
- **401 Unauthorized**: Returned if the Spotify API credentials are invalid.
- **500 Internal Server Error**: Returned if there is an issue with the Spotify API or server.

Feel free to add more detailed examples and explanations to suit your needs. This should make the README more user-friendly and informative!
