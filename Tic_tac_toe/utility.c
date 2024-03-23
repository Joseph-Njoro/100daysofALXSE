#include "utility.h"

void initialize_board(char board[3][3]) {
    // Initialize the game board with empty spaces
    for (int i = 0; i < 3; i++) {
        for (int j = 1; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}