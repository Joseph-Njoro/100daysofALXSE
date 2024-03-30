#include <stdio.h>

void cycleSort(int arr[], int n) {
    for (int start = 0; start <= n - 2; start++) {
        int item = arr[start];
        int pos = start;
        for (int i = start + 1; i < n; i++) {
            if (arr[i] < item) {
                pos++;
            }
        }
        if (pos == start) {
            continue;
        }
        while (item == arr[pos]) {
            pos++;
        }
        if (pos != start) {
            int temp = arr[pos];
            arr[pos] = item;
            item = temp;
        }
        while (pos != start) {
            pos = start;
            for (int i = start + 1; i < n; i++) {
                if (arr[i] < item) {
                    pos++;
                }
            }
            while (item == arr[pos]) {
                pos++;
            }
            if (item != arr[pos]) {
                int temp = arr[pos];
                arr[pos] = item;
                item = temp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    cycleSort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}