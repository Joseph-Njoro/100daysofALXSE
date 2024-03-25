#include <stdio.h>

int main() {
    int num = 5; // Binary: 0101

    int n = 2; // Bit to check (0-based index)
    int iSet = (num >> n) & 1; // Check if nth bit is set

    printf("Bit %d is %s\n", n, isSet ? "Set" : "Not set");

    return 0;
}