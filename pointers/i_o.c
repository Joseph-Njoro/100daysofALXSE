#include <stdio.h>

int main() {
    char str[20];

    // Input string from user
    printf("Enter a string: ");
    scanf("%s", str); // Note: %s does not need & for arrays
    printf("You entered: %s\n", str);

    return 0;
}