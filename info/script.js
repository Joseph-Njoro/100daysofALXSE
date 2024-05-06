// script.js
window.onload = function() {
    document.getElementById('submit-btn').addEventListener('click', function() {
        const ipAddress = document.getElementById('ip-address').value;
        if (ipAddress.trim() !== '') {
            fetchIPDetails(ipAddress);
        } else {
            alert('Please enter a valid IP address.');
        }
    });
}

function fetchIPDetails(ipAddress) {
    fetch(`https://ipinfo.io/${ipAddress}/json?token=b389ffaad2bc64`)
        .then(response => response.json())
        .then(data => {
            const ipInfoDiv = document.getElementById('ip-info');
            ipInfoDiv.innerHTML = `
                <p><strong>IP Address:</strong> ${data.ip}</p>
                <p><strong>City:</strong> ${data.city}</p>
                <p><strong>Region:</strong> ${data.region}</p>
                <p><strong>Country:</strong> ${data.country}</p>
                <p><strong>Postal Code:</strong> ${data.postal}</p>
                <p><strong>Timezone:</strong> ${data.timezone}</p>
                <p><strong>ISP:</strong> ${data.org}</p>
            `;
            fetchMap(data.loc.split(',')[0], data.loc.split(',')[1]);
        })
        .catch(error => console.error('Error fetching IP details:', error));
}

function fetchMap(latitude, longitude) {
    // Create a new Leaflet map instance with the provided latitude and longitude
    const map = L.map('map').setView([latitude, longitude], 13);

    // Add the OpenStreetMap tile layer to the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Add a marker to the map at the specified location
    L.marker([latitude, longitude]).addTo(map)
        .bindPopup('Your Location') // Add a popup with the text "Your Location"
        .openPopup(); // Open the popup by default
}
