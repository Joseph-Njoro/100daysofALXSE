#include <stdio.h>

int main() {
    int a = 5; // Binary: 0101

    int result = ~a; // Bitwise NOT
    printf("Result of ~%d = %d\n", a, result);

    return 0;
}