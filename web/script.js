function showArtistSearch() {
    clearResults();
    const searchInputs = document.getElementById('searchInputs');
    searchInputs.innerHTML = `
      <input type="text" id="artistQuery" placeholder="Enter artist name...">
      <button onclick="searchArtists()">Search</button>
    `;
  }
  
  function showTrackSearch() {
    clearResults();
    const searchInputs = document.getElementById('searchInputs');
    searchInputs.innerHTML = `
      <input type="text" id="trackQuery" placeholder="Enter track name...">
      <button onclick="searchTracks()">Search</button>
    `;
  }
  
  function showTopTracks() {
    clearResults();
    fetchTopTracks();
  }
  
  function searchArtists() {
    const artistQuery = document.getElementById('artistQuery').value.trim();
    if (artistQuery === '') {
      alert('Please enter an artist name');
      return;
    }
    fetch(`https://matchmytaste.onrender.com/search_artist`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query: artistQuery })
    })
    .then(response => response.json())
    .then(data => displayResults(data, 'artist'))
    .catch(error => {
      console.error('Error fetching data:', error);
      alert('Error fetching data. Please try again later.');
    });
  }
  
  function searchTracks() {
    const trackQuery = document.getElementById('trackQuery').value.trim();
    if (trackQuery === '') {
      alert('Please enter a track name');
      return;
    }
    fetch(`https://matchmytaste.onrender.com/search_track`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query: trackQuery })
    })
    .then(response => response.json())
    .then(data => displayResults(data, 'track'))
    .catch(error => {
      console.error('Error fetching data:', error);
      alert('Error fetching data. Please try again later.');
    });
  }
  
  function fetchTopTracks() {
    clearResults();
    fetch(`https://matchmytaste.onrender.com/top_tracks_of_month`, {
      method: 'GET',
      headers: {
        'accept': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => displayResults(data, 'top_tracks'))
    .catch(error => {
      console.error('Error fetching data:', error);
      alert('Error fetching data. Please try again later.');
    });
  }
  
  function displayResults(data, type) {
    const resultsContainer = document.getElementById('resultsContainer');
    resultsContainer.innerHTML = '';
  
    switch (type) {
      case 'artist':
        data.forEach(item => {
          const card = createCard(item.name, `Artist: ${item.name}`, item.url);
          resultsContainer.appendChild(card);
        });
        break;
      case 'track':
        data.forEach(item => {
          const card = createCard(item.name, `Track by ${item.artists}`, item.url);
          resultsContainer.appendChild(card);
        });
        break;
      case 'top_tracks':
        data.forEach(track => {
          const card = createCard(track.name, `Artist: ${track.artists}`, track.url);
          resultsContainer.appendChild(card);
        });
        break;
    }
  }
  
  function createCard(name, subtitle, url) {
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
      <h3>${name}</h3>
      <p>${subtitle}</p>
      <a href="${url}" target="_blank">Listen on Spotify</a>
    `;
    return card;
  }
  
  function clearResults() {
    const resultsContainer = document.getElementById('resultsContainer');
    resultsContainer.innerHTML = '';
    const searchInputs = document.getElementById('searchInputs');
    searchInputs.innerHTML = '';
  }
  