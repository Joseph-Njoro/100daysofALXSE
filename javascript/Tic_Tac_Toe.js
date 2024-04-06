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

// Function to reset the gameaconst readline = require('readline');

class TicTacToe {
    constructor() {
        this.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ];
        this.currentPlayer = 'X';
        this.movesLeft = 9;
        this.gameOver = false;
    }

    printBoard() {
        console.log('  1 2 3');
        for (let i = 0; i < 3; i++) {
            console.log(`${i + 1} ${this.board[i].join(' ')}`);
        }
    }

    isValidMove(row, col) {
        return this.board[row][col] === '-';
    }

    makeMove(row, col) {
        if (this.isValidMove(row, col)) {
            this.board[row][col] = this.currentPlayer;
            this.movesLeft--;
            this.checkWinner(row, col);
            this.switchPlayer();
        } else {
            console.log('Invalid move. Try again.');
        }
    }

    switchPlayer() {
        this.currentPlayer = (this.currentPlayer === 'X') ? 'O' : 'X';
    }

    checkWinner(row, col) {
        if (this.checkRow(row) || this.checkColumn(col) || this.checkDiagonal(row, col)) {
            this.gameOver = true;
            console.log(`Player ${this.currentPlayer} wins!`);
        } else if (this.movesLeft === 0) {
            this.gameOver = true;
            console.log('It\'s a draw!');
        }
    }

    checkRow(row) {
        return (this.board[row][0] === this.currentPlayer &&
                this.board[row][1] === this.currentPlayer &&
                this.board[row][2] === this.currentPlayer);
    }

    checkColumn(col) {
        return (this.board[0][col] === this.currentPlayer &&
                this.board[1][col] === this.currentPlayer &&
                this.board[2][col] === this.currentPlayer);
    }

    checkDiagonal(row, col) {
        if (row === col || row + col === 2) {
            return ((this.board[0][0] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][2] === this.currentPlayer) ||
                    (this.board[0][2] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][0] === this.currentPlayer));
        }
        return false;
    }
}

function main() {
    const ticTacToe = new TicTacToe();
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log('Welcome to Tic Tac Toe!\n');
    ticTacToe.printBoard();

    rl.on('line', (input) => {
        const [row, col] = input.trim().split(' ');
        if (!ticTacToe.gameOver && ticTacToe.isValidMove(row - 1, col - 1)) {
            ticTacToe.makeMove(row - 1, col - 1);
            ticTacToe.printBoard();
        } else if (!ticTacToe.gameOver) {
            console.log('Invalid move. Try again.');
        }
        if (ticTacToe.gameOver) {
            rl.close();
        }
    });
}

main();

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
playerMove(1, 0); // Player O moves to cell (1, 0)
playerMove(0, 2); // Player X moves to cell (0, 2)
// Continue playing...