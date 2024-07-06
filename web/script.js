async function searchArtist() {
    const query = document.getElementById('artist-query').value;
    if (!query) {
        alert('Please enter an artist name');
        return;
    }
    try {
        const response = await fetch('https://matchmytaste.onrender.com/search_artist', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Artist data:', data); // Log response data
        displayResults(data);
    } catch (error) {
        console.error('Error fetching artist data:', error);
        alert('An error occurred while fetching artist data');
    }
}

async function searchTrack() {
    const query = document.getElementById('track-query').value;
    if (!query) {
        alert('Please enter a track name');
        return;
    }
    try {
        const response = await fetch('https://matchmytaste.onrender.com/search_track', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Track data:', data); // Log response data
        displayResults(data);
    } catch (error) {
        console.error('Error fetching track data:', error);
        alert('An error occurred while fetching track data');
    }
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>No results found.</p>';
        return;
    }
    const list = document.createElement('ul');
    results.forEach(result => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<a href="${result.url}" target="_blank">${result.name}</a>`;
        list.appendChild(listItem);
    });
    resultsDiv.appendChild(list);
}
