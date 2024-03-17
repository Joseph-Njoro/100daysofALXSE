#include <stdio.h>

// Function to calculate factorial recursively
int factorial(int n) {
    // Base case
    if (n == 0) {
        return 1;
    }
    // Recursive case
    else {
        return n * factorial(n - 1);
    }
}

int main() {
    int n = 5;
    printf("Factorial of %d is %d\n", n, factorial(n));
    return 0;
}