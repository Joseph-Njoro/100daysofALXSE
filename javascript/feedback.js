// feedback.js

// Add event listeners for hover and click events
const cells = document.querySelectorAll('.cell');
cells.forEach(cell => {
  cell.addEventListener('mouseover', () => {
    cell.style.backgroundColor = 'lightgray';
  });

  cell.addEventListener('mouseout', () => {
    cell.style.backgroundColor = '';
  });

  cell.addEventListener('click', () => {
    if (cell.textContent === '') {
      cell.style.backgroundColor = 'yellow';
      cell.style.color = 'red';
    }
  });
});

// Add a text indicating which player is playing
const currentPlayerText = document.createElement('p');
currentPlayerText.id = 'current-player';
currentPlayerText.textContent = `Current player: ${currentPlayer}`;
document.body.appendChild(currentPlayerText);

// Update the text indicating which player is playing
cells.forEach(cell => {
  cell.addEventListener('click', () => {
    if (cell.textContent === '') {
      currentPlayerText.textContent = `Current player: ${currentPlayer}`;
    }
  });
});