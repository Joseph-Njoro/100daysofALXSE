// Initialize game board
let board = [
  ['', '', ''],
  ['', '', ''],
  ['', '', '']
];

// Initialize current player
let currentPlayer = 'X';

// Function to check for a winner
function checkWinner() {
  // Check rows, columns, and diagonals for a win
  for (let i = 0; i < 3; i++) {
    if (board[i][0] === currentPlayer &&
        board[i][1] === currentPlayer &&
        board[i][2] === currentPlayer) {
      return true; // Row win
    }
    if (board[0][i] === currentPlayer &&
        board[1][i] === currentPlayer &&
        board[2][i] === currentPlayer) {
      return true; // Column win
    }
  }
  if (board[0][0] === currentPlayer &&
      board[1][1] === currentPlayer &&
      board[2][2] === currentPlayer) {
    return true; // Diagonal win
  }
  if (board[0][2] === currentPlayer &&
      board[1][1] === currentPlayer &&
      board[2][0] === currentPlayer) {
    return true; // Diagonal win
  }
  return false; // No win
}

// Function to check for a draw
function checkDraw() {
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (board[i][j] === '') {
        return false; // Empty cell found, game not draw
      }
    }
  }
  return true; // All cells filled, game draw
}

// Function to handle player move
function playerMove(row, col) {
  if (board[row][col] === '') {
    board[row][col] = currentPlayer; // Set player's symbol
    if (checkWinner()) {
      alert(`Player ${currentPlayer} wins!`); // Display winner
      resetGame();
    } else if (checkDraw()) {
      alert('It\'s a draw!'); // Display draw
      resetGame();
    } else {
      currentPlayer = currentPlayer === 'X' ? 'O' : 'X'; // Switch players
    }
  } else {
    alert('Cell already occupied! Choose another.');
  }
}

// Function to reset the game
function resetGame() {
  board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
  ];
  currentPlayer = 'X';
}

// Example usage:
playerMove(0, 0); // Player X moves to cell (0, 0)
playerMove(1, 1); // Player O moves to cell (1, 1)
playerMove(0, 1); // Player X moves to cell (0, 1)
playerMove(1 0); // Player O moves to cell (1, 0)
playerMove(0, 2) // Player X moves to cell (0, 2)