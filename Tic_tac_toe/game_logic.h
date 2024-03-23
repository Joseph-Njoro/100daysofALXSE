#ifndef GAME_LOGIC_H
#define GAME_LOGIC_H

int check_winner(char board[3][3]);
int is_board_full(char board[3][3]);
char get_current_player();
void switch_player();

#endif /* GAME_LOGIC_H */