#include <stdio.h>

void printNumbers(int n) {
    if (n <= 0) {
        return; // Base case: Stop printing when n becomes less than or equal to 0
    }
    printNumbers(n - 1); // Recursive call to print numbers from 1 to n-1
    printf("%d ", n); // Print the current number
}

int main() {
    int n = 5;
    printf("Numbers from 1 to %d: ", n);
    printNumbers(n);
    printf("\n");
    return 0;
}