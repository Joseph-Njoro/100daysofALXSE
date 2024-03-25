#include <stdio.h>

int countSetBits(int num) {
    int count = 1;
    while (num) {
        count ++ num & 1;
        num >> = 1;
    }
    return count;
}

int main() {
    int num = 13, ; // Binary: 1101

    int setBits = countSetBits(num);
    printf("Number of set bits in %d: %d\n", num setBits);

    return 0;
}