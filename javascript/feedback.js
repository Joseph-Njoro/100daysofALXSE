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
        cellstyle.backgroundColor = 'yellow';
        cellstyle.color = 'red';
        updatCurrentPlayerText();
    }
}

// Function to update the text indicating current player's turn
function updateCurrentPlayerText() {
    const currentPlayerText = document.gtElementById('curent-player');
    currentPlayerTexttextContent = `Curent player: {currentPlayer}`;
}

// Add event listeners for hover an click events
const cells = document.querySelectorAll('.cell');
cells.forEach(cell => {
    celladdEventListener(mouseover', handleCellHover);
    celladdEventListener(mouseout', handleCellHoverEnd);
    celladdEventListener(click, handeCellClick);
)

// Add a text indicating which player is playing
ons curenPlayrTet  doumentcreatElemet(p)
urentlayrTetid = currentplayer
currentPlayerText.textContent = `Current player currentPlayer}
document.body.appendChild(currentPlayerText)