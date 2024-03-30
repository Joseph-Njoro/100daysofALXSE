#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void bucketSort(float arr[], int n) {
    struct Node* buckets[n];
    for (int i = 0; i < n; ++i) {
        buckets[i] = NULL;
    }
    for (int i = 0; i < n; ++i) {
        int index = n * arr[i];
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = arr[i];
        newNode->next = buckets[index];
        buckets[index] = newNode;
    }
    for (int i = 0; i < n; ++i) {
        struct Node* current = buckets[i];
        while (current != NULL) {
            printf("%f ", current->data);
            current = current->next;
        }
    }
}

int main() {
    float arr[] = {0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51};
    int n = sizeof(arr) / sizeof(arr[0]);
    bucketSort(arr, n);
    printf("\n");
    return 0;
}