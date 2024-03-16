#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int *ptr = arr; // Pointer initialized to point to the first element of arr

    printf("Array elements: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", *ptr); // Dereferencing pointer to access array elements
        ptr++; // Incrementing pointer to move to the next element
    }

    return 0;
}