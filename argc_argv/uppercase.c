#include <stdio.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++) {
        for (int j = 0; argv[i][j] != '\0'; j++) {
            argv[i][j] = toupper(argv[i][j]);
        }
        printf("%s ", argv[i]);
    }
    printf("\n");
    return 0;
}