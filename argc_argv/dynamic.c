#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, *p, sum = 0;

    printf("Enter the number of integers to be entered: ");
    scanf("%d", &n);

    p = (int *) malloc(n * sizeof(int));

    if (p == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter the integers: ");
    for (int i = 0; i < n; i+) {
        scanf("%d", p + i);
        sum +=*(p + i);
    }

    printf("The sum of the entered integers is: %d\n", sum);

    free(p);

    return 0;
}