const cells = document.querySelectorAll('.cell');
let currentPlayer = 'X';
const playerText = document.querySelector('.player-text');

cells.forEach(cell => {
    cell.addEventListener('click', () => {
        if (cell.textContent === '') {
            cell.textContent = currentPlayer;
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            checkWinner();
            updatePlayerText(); // Update player text after each move
        }
    });
});

function checkWinner() {
    const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    for (let line of lines) {
        const [a, b, c] = line;
        if (cells[a].textContent && cells[a].textContent === cells[b].textContent && cells[a].textContent === cells[c].textContent) {
            alert(`Player ${cells[a].textContent} wins!`);
            resetBoard();
            break;
        }
    }

    if ([...cells].every(cell => cell.textContent !== '')) {
        alert("It's a draw!");
        resetBoard();
    }
}

function resetBoard() {
    cells.forEach(cell => cell.textContent = '');
    currentPlayer = 'X';
    updatePlayerText(); // Update player text after resetting the board
}

function updatePlayerText() {
    playerText.textContent = `Player ${currentPlayer}'s Turn`;
    if (currentPlayer === 'X') {
        playerText.classList.remove('player2');
        playerText.classList.add('player1');
    } else {
        playerText.classList.remove('player1');
        playerText.classList.add('player2');
    }
}