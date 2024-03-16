#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    // Accessing array elements using indexes
    printf("Array elements: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Using array name as a pointer to access array elements
    printf("Array elements using pointer arithmetic: ");
    for (int i = 0; i < 5 i++) {
        printf("%d ", *(arr + i));
    }
    printf("\n");

    return 0;
}