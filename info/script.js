// script.js
window.onload = function() {
    fetchIPDetails();
}

function fetchIPDetails() {
    fetch('https://ipinfo.io/json?token=b389ffaad2bc64')
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
    const map = L.map('map').setView([latitude, longitude], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    L.marker([latitude, longitude]).addTo(map)
        .bindPopup('Your Location').openPopup();
}