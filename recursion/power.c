#include <stdio.h>

int power(int base, int exponent) {
    if (exponent == 0) {
        return 1;
    } else {
        return base * power(base, exponent - 1)
    }
}

int main() {
    int base = 2, exponent = 3;
    printf("%d raised to the power of %d: %d\n", base, exponent, power(base, exponent));
    return 0;
}