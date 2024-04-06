// feedback.js

// Function to handle hover effect on cells
function handleCellHover(cell) {
    cell.style.backgroundColor = 'lightgray';
}

// Function to handle removing hover effect on cells
function handleCellHoverEnd(cell) {
    cell.style.backgroundColor = '';
}

// Function to handle click event on cells
function handleCellClick(cell) {
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
    cell.addEventListener('mouseover', () => {
        handleCellHover(cell);
    });

    cell.addEventListener('mouseout', () => {
        handleCellHoverEnd(cell);
    });

    cell.addEventListener('click', () => {
        handleCellClick(cell);
    });
});

// Add a text indicating which player is playing
const currentPlayerText = document.createElement('p');
currentPlayerText.id = 'current-player';
currentPlayerText.textContent = `Current player: ${currentPlayer}`;
document.body.appendChild(currentPlayerText);