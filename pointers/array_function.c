#include <stdio.h>

// Function to print the elements of an array
void printArray(int arr[], int size) {
    printf("Array elements: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};

    // Passing the array to the printArray function
    printArray(arr, 5);

    return 0;
}