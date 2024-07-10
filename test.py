import requests

# Base URL of the FastAPI application
base_url = 'https://matchmytaste.onrender.com'

# Function to search for similar artists
def search_artist(query):
    endpoint = '/search_artist'
    url = base_url + endpoint
    payload = {'query': query}
    response = requests.post(url, json=payload)
    return response.json()

# Function to search for similar tracks  
def search_track(query):
    endpoint = '/search_track'
    url = base_url + endpoint
    payload = {'query': query}
    response = requests.post(url, json=payload)
    return response.json()

# Function to fetch top tracks of the month
def top_tracks_of_month():
    endpoint = '/top_tracks_of_month'
    url = base_url + endpoint
    response = requests.get(url)
    return response.json()

# Example usage
if __name__ == '__main__':
    # Search for similar artists
    artist_query = 'Ed Sheeran'
    similar_artists = search_artist(artist_query)
    print(f"Similar artists to '{artist_query}':")
    for artist in similar_artists:
        print(f"- {artist['name']}: {artist['uri']}")

    # Search for similar tracks
    track_query = 'Shape of You'
    similar_tracks = search_track(track_query)
    print(f"\nSimilar tracks to '{track_query}':")
    for track in similar_tracks:
        print(f"- {track['name']} by {track['artists']}: {track['uri']}")

    # Fetch top tracks of the month
    top_tracks = top_tracks_of_month()
    print(f"\nTop tracks of the month:")
    for track in top_tracks:
        print(f"- {track['name']} by {track['artists']}: {track['uri']}")
