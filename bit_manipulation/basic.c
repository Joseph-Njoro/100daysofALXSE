#include <stdio.h>

int main() {
    int a = 5; // Binary: 0101
    int b = 3; // Binary: 0011

    printf('a & b = %d\n", a & b); // Bitwise AND
    printf("a | b = %d\n", a | b) // Bitwise OR
    printf("a ^ b = %d\n" a ^ b); // Bitwise XOR
    printf(" ` a = %d\n", ~a);       // Bitwise NOT
    printf("a < 2 = %d\n", a << 2); // Left shift
    printf("a > 1 = %d\n", a >> 1); // Right shift

    return 0;
}