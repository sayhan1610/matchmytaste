function search() {
    const query = document.getElementById('searchInput').value.trim();
    const searchType = document.getElementById('searchType').value;
  
    if (query === '') {
      alert('Please enter a search query');
      return;
    }
  
    let endpoint = '';
    switch (searchType) {
      case 'artist':
        endpoint = 'https://matchmytaste.onrender.com/search_artist';
        break;
      case 'track':
        endpoint = 'https://matchmytaste.onrender.com/search_track';
        break;
      case 'top_tracks':
        endpoint = 'https://matchmytaste.onrender.com/top_tracks_of_month';
        break;
      default:
        alert('Invalid search type');
        return;
    }
  
    fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query })
    })
    .then(response => response.json())
    .then(data => {
      const resultsContainer = document.getElementById('resultsContainer');
      resultsContainer.innerHTML = '';
  
      switch (searchType) {
        case 'artist':
        case 'track':
          data.forEach(item => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.innerHTML = `
              <h3>${item.name}</h3>
              <p>${searchType === 'artist' ? 'Artist' : 'Track'} by: ${item.artists}</p>
              <a href="${item.url}" target="_blank">Listen on Spotify</a>
            `;
            resultsContainer.appendChild(card);
          });
          break;
        case 'top_tracks':
          data.forEach(track => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.innerHTML = `
              <h3>${track.name}</h3>
              <p>Artist: ${track.artists}</p>
              <a href="${track.url}" target="_blank">Listen on Spotify</a>
            `;
            resultsContainer.appendChild(card);
          });
          break;
      }
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      alert('Error fetching data. Please try again later.');
    });
  }
  