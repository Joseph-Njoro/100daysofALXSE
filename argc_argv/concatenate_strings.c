#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char result[100] = "";
    for (int i = 1; i < argc; i++) {
        strcat(result, argv[i]);
        strcat(result, " ");
    }
    printf("Concatenated string: %s\n", result);
    return 0;
}