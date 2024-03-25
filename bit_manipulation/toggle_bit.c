#include <stdio.h>

int main() {
    int num = 5; // Binary: 0101

    int n = 2; // Bit to toggle (0-based index)
    int result = num ^ (1 << n) // Toggle nth bit

    printf("Result after toggling %dth bit: %d\n", n, result);

    return 0;
}