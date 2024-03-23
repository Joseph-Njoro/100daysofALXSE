#include <ncurses.h>
#include "tic_tac_toe.h"

// Function to draw the tic-tac-toe board using ncurses
void draw_board(char board[3][3]) {
    clear(); // Clear the screen
    int row, col;
    for(row = 0; row < 3; row++) {
        for(col = 0; col < 3; col++) {
            mvprintw(row * 2, col * 4, "%c", board[row][col]);
            if(col < 2) {
                printw(" | ");
            }
        }
        if(row < 2) {
            printw("\n-----------\n");
        }
    }
    refresh(); // Refresh the screen
}

int main() {
    // Initialize ncurses
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    // Game board
    char board[3][3];
    initialize_board(board);

    // Main game loop
    while(1) {
        draw_board(board);

        // Get the current player's move
        int row, col;
        get_move(board, &row, &col);

        // Update the board with the player's move
        update_board(board, row, col);

        // Check if the game is over
        if(check_winner(board)) {
            draw_board(board);
            printw("Player %c wins!\n", get_current_player());
            break;
        } else if(is_board_full(board)) {
            draw_board(board);
            printw("It's a draw!\n");
            break;
        }

        // Switch players for the next turn
        switch_player();
    }

    // Clean up ncurses
    getch();
    endwin();

    return 0;
}