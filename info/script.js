// script.js
class IpInfoContainer {
    constructor(containerElement) {
        this.containerElement = containerElement;
        this.ipAddressInput = containerElement.querySelector('#ip-address');
        this.submitButton = containerElement.querySelector('#submit-btn');
        this.ipInfoElement = containerElement.querySelector('#ip-info');
        this.userAgentElement = containerElement.querySelector('#userAgent');
        this.mapElement = document.getElementById('map');

        this.submitButton.addEventListener('click', this.getIpInfo.bind(this));
        this.detectUserAgent();
    }

    detectUserAgent() {
        const userAgent = navigator.userAgent;
        this.userAgentElement.innerText = "User Agent: " + userAgent;
    }

    getIpInfo() {
        const ipAddress = this.ipAddressInput.value;
        if (ipAddress.trim()!== '') {
            this.fetchIPDetails(ipAddress);
        } else {
            alert('Please enter a valid IP address.');
        }
    }

    fetchIPDetails(ipAddress) {
        fetch(`https://ipinfo.io/${ipAddress}/json?token=b389ffaad2bc64`)
           .then(response => response.json())
           .then(data => {
                const ipInfoHtml = `
                    <p><strong>IP Address:</strong> ${data.ip}</p>
                    <p><strong>City:</strong> ${data.city}</p>
                    <p><strong>Region:</strong> ${data.region}</p>
                    <p><strong>Country:</strong> ${data.country}</p>
                    <p><strong>Postal Code:</strong> ${data.postal}</p>
                    <p><strong>Timezone:</strong> ${data.timezone}</p>
                    <p><strong>ISP:</strong> ${data.org}</p>
                `;
                this.ipInfoElement.innerHTML = ipInfoHtml;
                this.fetchMap(data.loc.split(',')[0], data.loc.split(',')[1]);
            })
           .catch(error => console.error('Error fetching IP details:', error));
    }

    fetchMap(latitude, longitude) {
        // Create a new Leaflet map instance with the provided latitude and longitude
        const map = L.map(this.mapElement).setView([latitude, longitude], 13);

        // Add the OpenStreetMap tile layer to the map
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Add a marker to the map at the specified location
        L.marker([latitude, longitude]).addTo(map)
           .bindPopup('Your Location') // Add a popup ihtetx Yu oain
           .openPopup(); // Open the popup by default
    }
}

const containerElement = document.querySelector('.container');
const ipInfoContainer = new IpInfoContainer(containerElement);