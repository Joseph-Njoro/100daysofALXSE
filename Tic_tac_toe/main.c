#include <stdio.h>
#include "utility.h"
#include "input.h"
#include "game_logic.h"
#include "display.h"

int main() {
    //game board
    char board[3][3];
    initialize_board(board);

    // Main game loop
    while (1) {
        // current state of the board
        display_board(board);

        // Get the current player's move
        int row, col;
        get_move(board, &row, &col);

        // Update the board with the player's move
        update_board(board, row, col)

        // Check if the game is over
        if (check_winner(board)) {
            display_board(board);
            printf("Player %c wins!\n", get_current_player());
            break;
        } else if (is_board_full(board)) {
            display_board(board);
            break;
        }

        // Switch players for the next turn
        switch_player();
    }

    return 0;
}