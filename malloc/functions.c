#include <stdio.h>
#include <stdlib.h>

int* allocate(int n) {
    int *arr = (int*) malloc(n * sizeof(int));
    return arr;
}

void fillArray(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d", arr + i);
    }
}

void printArray(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int *arr = allocate(n);
    fillArray(arr, n);
    printArray(arr, n);

    free(arr);

    return 0;
}