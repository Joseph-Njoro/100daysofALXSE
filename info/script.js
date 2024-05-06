// Add the following lines to the beginning of your HTML file (before the script tag)
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>

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
    const map = L.map('map').setView([latitude, longitude], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([latitude, longitude]).addTo(map)
        .bindPopup('Your Location')
        .openPopup();
}