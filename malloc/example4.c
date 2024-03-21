#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int *arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory not allocated");
        exit(0);
    }

    printf("Enter the elements: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("The elements of the array are: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}