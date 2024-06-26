import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime

# Replace with your own Spotify API credentials
SPOTIPY_CLIENT_ID = 'e1212180fa8d43bdac68a2e39697350b'
SPOTIPY_CLIENT_SECRET = 'secret'

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

def get_songs_by_date(month, day):
    # Format the query for release date
    query = f'release_date:{month:02d}-{day:02d}'
    results = sp.search(q=query, type='track', limit=50)
    tracks = results['tracks']['items']
    
    # Sort tracks by popularity (number of streams)
    sorted_tracks = sorted(tracks, key=lambda x: x['popularity'], reverse=True)
    
    # Return the top 5 tracks
    return sorted_tracks[:5]

def main():
    # Get the current date
    today = datetime.date.today()
    month = today.month
    day = today.day
    
    # Fetch top 5 songs released on this date
    top_songs = get_songs_by_date(month, day)
    
    # Print the top 5 songs
    print(f"Top 5 songs released on {today.strftime('%B %d')}:")
    for idx, song in enumerate(top_songs, start=1):
        artist_names = ', '.join(artist['name'] for artist in song['artists'])
        print(f"{idx}. {song['name']} by {artist_names} (Popularity: {song['popularity']})")

if __name__ == "__main__":
    main()
