#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0) {
            printf("Verbose mode enabled.\n");
            break;
        }
    }
    return 0;
}