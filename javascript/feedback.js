// feedback.js

// Function to handle hover effect on cells
function handleCellHover(event) {
    const cell = event.target;
    cell.style.backgroundColor = 'lightgray';
}

// Function to handle removing hover effect on cells
function handleCellHoverEnd(event) {
    const cell = event.target;
    cell.style.backgroundColor = '';
}

// Function to handle click event on cells
function handleCellClick(event) {
    const cell = event.target;
    if (cell.textContent === '') {
        cell.style.backgroundColor = 'yellow';
        cell.style.color = 'red';
        updateCurrentPlayerText();
    }
}

// Function to update the text indicating current player's turn
function updateCurrentPlayerText() {
    const currentPlayerText = document.getElementById('current-player');
    currentPlayerText.textContent = `Current player: ${currentPlayer}`;
}

// Add event listeners for hover and click events
const cells = document.querySelectorAll('.cell');
cells.forEach(cell => {
    cell.addEventListener('mouseover', handleCellHover);
    cell.addEventListener('mouseout', handleCellHoverEnd);
    cell.addEventListener('click', handleCellClick);
});

// Add a text indicating which player is playing
ons curenPlayerText = document.createElement('p');
urentlayrTetid = currentplayer
currentPlayerText.textContent = `Current player currentPlayer}
document.body.appendChild(currentPlayerText)