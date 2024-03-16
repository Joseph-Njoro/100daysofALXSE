#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;

    ptr = (int *)malloc(sizeof(int)); // Dynamic memory allocation
    if (ptr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    *ptr = 10; // Storing value in dynamically allocated memory

    printf("Value stored in dynamically allocated memory: %d\n", *ptr);

    free(ptr); // Freeing dynamically allocated memory

    return 0;
}