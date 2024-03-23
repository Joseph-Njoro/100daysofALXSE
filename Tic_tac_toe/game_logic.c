#include "tic_tac_toe.h"

void update_board(char board[3][3], int row, int col) {
    char current_player = get_current_player();
    
    // Check if the chosen position is empty
    if (board[row][col] == ' ') {
        // Update the board with the current player's symbol
        board[row][col] = current_player;
    } else {
        // Print an error message if the position is already occupied
        printf("Error: This position is already occupied. Please choose another position.\n");
    }
}

int check_winner(char board[3][3]) {
    // Check rows
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ') {
            return board[i][0]; // Winner found
        }
    }

    // Check columns
    for (int j = 0; j < 3; ++j) {
        if (board[0][j] == board[1][j] && board[1][j] == board[2][j] && board[0][j] != ' ') {
            return board[0][j]; // Winner found
        }
    }

    // Check diagonals
    if ((board[0][0] == board[1][1] && board[1][1] == board[2][2]) ||
        (board[0][2] == board[1][1] && board[1][1] == board[2][0])) {
        return board[1][1]; // Winner found
    }

    return 0; // No winner
}

int is_board_full(char board[3][3]) {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == ' ') {
                return 0; // Board is not full
            }
        }
    }
    return 1; // Board is full
}

char get_current_player() {
    static char current_player = 'X'; // Player X starts
    return current_player;
}

void switch_player() {
    static char current_player = 'X'; // Player X starts
    if (current_player == 'X') {
        current_player = 'O';
    } else {
        current_player = 'X';
    }
}