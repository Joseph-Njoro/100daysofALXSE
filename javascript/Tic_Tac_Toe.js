const readline = require('readline');

class TicTacToe {
    constructor() {
        this.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']];
        this.currentPlayer = 'X';
    }

    resetBoard() {
        this.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']];
        this.currentPlayer = 'X';
    }

    isValidMove(row, col) {
        return this.board[row][col] === '-';
    }

    makeMove(row, col) {
        this.board[row][col] = this.currentPlayer;
        this.switchPlayer();
    }

    isFull() {
        return this.board.every(row => row.every(cell => cell !== '-'));
    }

    isWinner() {
        // Check rows
        for (let i = 0; i < 3; i++) {
            if (this.board[i][0] === this.currentPlayer && this.board[i][1] === this.currentPlayer && this.board[i][2] === this.currentPlayer) {
                return true;
            }
        }

        // Check columns
        for (let i = 0; i < 3; i++) {
            if (this.board[0][i] === this.currentPlayer && this.board[1][i] === this.currentPlayer && this.board[2][i] === this.currentPlayer) {
                return true;
            }
        }

        // Check diagonals
        if (this.board[0][0] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][2] === this.currentPlayer) {
            return true;
        }
        if (this.board[0][2] === this.currentPlayer && this.board[1][1] === this.currentPlayer && this.board[2][0] === this.currentPlayer) {
            return true;
        }

        return false;
    }

    switchPlayer() {
        this.currentPlayer = this.currentPlayer === 'X' ? 'O' : 'X';
    }

    printBoard() {
        for (let i = 0; i < 3; i++) {
            console.log(` | ${this.board[i][0]} | ${this.board[i][1]} | ${this.board[i][2]} | `);
            if (i < 2) {
                console.log(' |---+---+---| ');
            }
        }
        console.log();
    }

    async playerMove() {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        return new Promise((resolve, reject) => {
            rl.question(`Player ${this.currentPlayer}, enter a row and column (e.g. 1 2): `, (input) => {
                const [row, col] = input.split(' ').map(val => parseInt(val) - 1);
                rl.close();
                if (isNaN(row) || isNaN(col) || row < 0 || row > 2 || col < 0 || col > 2) {
                    console.log('Invalid input. Please try again.');
                    resolve(this.playerMove());
                } else if (!this.isValidMove(row, col)) {
                    console.log('Invalid move. Please try again.');
                    resolve(this.playerMove());
                } else {
                    resolve({ row, col });
                }
            });
        });
    }

    async play() {
        console.log('Welcome to Tic Tac Toe!\n');
        this.printBoard();
        while (!this.isFull()) {
            const { row, col } = await this.playerMove();
            this.makeMove(row, col);
            this.printBoard();
            if (this.isWinner()) {
                console.log(`Player ${this.currentPlayer} wins!`);
                return;
            }
        }
        console.log("It's a draw!");
    }
}

const game = new TicTacToe();
game.play();