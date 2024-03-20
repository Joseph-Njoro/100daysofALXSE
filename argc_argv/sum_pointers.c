#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = sizeof(arr) / sizeof(arr[0]);
    int *p, sum = 0;

    p = arr;
    for (int i = 0; i < size; i++) {
        sum += *p;
        p++;
    }

    printf("The sum of the array is: %d\n", sum);

    return 0;
}