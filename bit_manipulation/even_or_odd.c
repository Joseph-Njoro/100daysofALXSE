#include <stdio.h>

int main() {
    int num = 6; // Example number

    if (num & 1) {
        printf("%d is Odd\n", num);
    } else {
        printf("%d is Even\n", num);
    }

    return 0;
}