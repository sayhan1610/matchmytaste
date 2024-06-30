import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import datetime

# Spotify credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_related_artists(artist_name, limit=50):
    # Fetch related artists for the given artist name
    results = sp.search(q=artist_name, type='artist', limit=1)
    artists = results['artists']['items']
    if artists:
        artist_id = artists[0]['id']
        related_artists = sp.artist_related_artists(artist_id)['artists']
        return related_artists[:limit]
    else:
        return []

def get_similar_tracks(track_name, limit=50):
    # Fetch recommended tracks based on the given track name
    results = sp.search(q=track_name, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        track_id = tracks[0]['id']
        recommended_tracks = sp.recommendations(seed_tracks=[track_id], limit=limit)['tracks']
        return recommended_tracks
    else:
        return []

def get_top_tracks_of_month(limit=50):
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
    results = sp.search(q=f'year:{year} month:{month}', type='track', limit=limit)
    top_tracks = results['tracks']['items']
    return top_tracks

def main():
    print("Welcome to the Spotify recommendation system!")
    print("Choose an option:")
    print("1. Search for similar artists")
    print("2. Search for similar tracks")
    print("3. Fetch top 50 tracks of the month")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Search for similar artists
        artist_name = input("Enter the name of the artist: ")
        similar_artists = get_related_artists(artist_name)
        artist_data = [{'name': artist['name'], 'uri': artist['external_urls']['spotify']} for artist in similar_artists]
        print(json.dumps(artist_data, indent=2))

    elif choice == '2':
        # Search for similar tracks
        track_name = input("Enter the name of the track: ")
        similar_tracks = get_similar_tracks(track_name)
        track_data = [{'name': track['name'], 'artists': ', '.join([artist['name'] for artist in track['artists']]), 'uri': track['external_urls']['spotify']} for track in similar_tracks]
        print(json.dumps(track_data, indent=2))

    elif choice == '3':
        # Fetch top tracks of the month
        top_tracks = get_top_tracks_of_month()
        top_tracks_data = [{'name': track['name'], 'artists': ', '.join([artist['name'] for artist in track['artists']]), 'uri': track['external_urls']['spotify']} for track in top_tracks]
        print(json.dumps(top_tracks_data, indent=2))

    else:
        print("Invalid choice. Please enter '1', '2', or '3'.")

if __name__ == "__main__":
    main()
