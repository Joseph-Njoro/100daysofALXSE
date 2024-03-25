#include <stdio.h>

int main() {
    int a = 5; // Binary: 0101
    int b = 3; // Binary: 0011

    int result = a | b; // Bitwise OR
    printf("Result of %d | %d = %d\n", a, b, result);

    return 0;
}