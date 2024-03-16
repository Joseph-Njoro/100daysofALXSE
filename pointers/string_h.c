#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[20];

    // Copying a string
    strcpy(str2, str1);
    printf("Copied string: %s\n", str2);

    // Concatenating strings
    strcat(str2, " world!");
    printf("Concatenated string: %s\n", str2);

    // String length
    printf("Length of string: %zu\n", strlen(str2));

    // Comparing strings
    if (strcmp(str1, str2) == 0) {
        printf("Strings are equal\n");
    } else {
        printf("Strings are not equal\n");
    }

    return 0;
}