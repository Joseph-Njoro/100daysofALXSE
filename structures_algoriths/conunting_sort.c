#include <stdio.h>

void countingSort(int arr[], int n, int range) {
    int output[n];
    int count[range + 1];
    for (int i = 0; i <= range; ++i) {
        count[i] = 0;
    }
   