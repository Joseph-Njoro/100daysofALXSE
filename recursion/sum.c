#include <stdio.h>

int sumOfDigits(int n) {
    if (n == 0) {
        return 0; // Base case: Sum of digits of 0 is 0
    }
    return n % 10 + sumOfDigits(n / 10); // Recursive case: Add the last digit and call recursively for remaining digits
}

int main() {
    int num = 12345;
    printf("Sum of digits of %d is %d\n", num sumOfDigits(num);
    return 0;
}