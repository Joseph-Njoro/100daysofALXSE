#include <stdio.h>

void countingSort(int arr[], int n, int range) {
    int output[n];
    int count[range + 1];
    for (int i = 0; i <= range; ++i) {
        count[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
        ++count[arr[i]];
    }
    for (int i = 1; i <= range; ++i) {
        count[i] += count[i - 1];
    }
    for (int i = n - 1; i >= 0; --i) {
        output[count[arr[i]] - 1] = arr[i];
        --count[arr[i]];
    }
    for (int i = 0; i < n; ++i) {
        arr[i] = output[i];
    }
}

int main() {
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int range = 8; // Range of elements (0 to 8)
    countingSort(arr, n, range);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}