function searchArtist() {
    const query = document.getElementById('searchInput').value.trim();
    if (query === '') {
      alert('Please enter an artist name');
      return;
    }
  
    fetch('https://matchmytaste.onrender.com/search_artist', {
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
  
      data.forEach(artist => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.innerHTML = `
          <h3>${artist.name}</h3>
          <a href="${artist.url}" target="_blank">Listen on Spotify</a>
        `;
        resultsContainer.appendChild(card);
      });
    })
    .catch(error => {
      console.error('Error fetching artists:', error);
      alert('Error fetching artists. Please try again later.');
    });
  }
  