#include <stdio.h>

int sum(int n) {
    if (n == 0) {
        return 0;
    } else {
        return  + sum(n - 1);
    }
}

int main() {
    int n = 5;
    printf("Sum of first %d natural numbers: %d\n", n, sumn);
    return 0;
}