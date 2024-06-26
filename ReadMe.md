# SongThisDay

SongThisDay is a simple Python script that finds the current date and prints the top 5 songs released on that date, sorted by the number of streams on Spotify.

## Features

- Fetches songs released on the current date (month and day).
- Sorts songs by popularity (number of streams).
- Prints the top 5 songs along with their artist names and popularity.

## Requirements

- Python 3.6+
- `spotipy` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/songthisday.git
   cd songthisday
   ```

2. Install the required Python packages:

   ```bash
   pip install spotipy
   ```

3. Set up your Spotify API credentials:

   - Create a Spotify Developer account and get your Client ID and Client Secret from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

4. Replace the placeholder credentials in the script with your own:
   ```python
   SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_ID'
   SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
   ```

## Usage

Run the script:

```bash
python songthisday.py
```
