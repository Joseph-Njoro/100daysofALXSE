#ifndef TIC_TAC_TOE_H
#define TIC_TAC_TOE_H

void initialize_board(char board[3][3]);
void get_move(char board[3][3], int *row, int *col);
int check_winner(char board[3][3]);
int is_board_full(char board[3][3]);
char get_current_player();
void switch_player();
void display_board(char board[3][3]);

#endif /* TIC_TAC_TOE_H */