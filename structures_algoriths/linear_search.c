#include <stdio.h>

int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; ++i) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1; // Target not found
}

int main() {
    int arr[] = {5, 3, 9, 2, 7};
    int target = 9;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = linearSearch(arr, n, target);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}