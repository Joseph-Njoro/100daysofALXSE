#include <stdio.h>

void find_max_and_replace(int *arr, int size, int *max_element) {
    *max_element = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > *max_element) {
            *max_element = arr[i];
        }
    }
}

void replace_max_with_zero(int *arr, int size, int max_element) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == max_element) {
            arr[i] = 0;
        }
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = sizeof(arr) / sizeof(arr[0]);
    int max_element;

    find_max_and_replace(arr, size, &max_element);
    replace_max_with_zero(arr, size, max_element);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}