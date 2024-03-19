#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    char *extension = strrchr(argv[1], '.');
    if (extension && strcmp(extension, ".c") == 0) {
        printf("File has a C source code extension.\n");
    } else {
        printf("File does not have a C source code extension.\n");
    }
    return 0;
}