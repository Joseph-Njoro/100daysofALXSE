#include <stdio.h>
#include "tic_tac_toe.h"

void get_move(char board[3][3], int *row, int *col) {
    // Get the player's move (row and column)
    printf("Enter your move (row column): ");
    scanf("%d %d", row, col);
}