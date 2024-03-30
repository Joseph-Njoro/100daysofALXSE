#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isArmstrong(int num) {
    int original = num;
    int sum = 0;
    int digits = (int)log10(num) + 1;
    while (num != 0) {
        int digit = num % 10;
        sum += pow(digit, digits);
        num /= 10;
    }
    return sum == original;
}

int main() {
    int num = 153;
    if (isArmstrong(num)) {
        printf("%d is an Armstrong number\n", num);
    } else {
        printf("%d is not an Armstrong number\n", num);
    }
    return 0;
}