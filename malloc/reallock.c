#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    int *newptr;
    int i, capacity = 1, size = 1;
    int element;

    ptr = (int*) malloc(capacity * sizeof(int));

    printf("Addresses of previously allocated memory: \n");
    for (i = 0; i < capacity; ++i) {
        printf("%p ", ptr + i);
    }

    printf("\nEnter elements: ");
    for (i = 0; i < capacity; ++i) {
        scanf("%d", ptr + i);
    }

    printf("\nEnter);
    return 0;