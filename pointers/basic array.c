#include <stdio.h>

int main() {
    // Declaration and initialization of an integer array
    int arr1[5] = {1, 2, 3, 4, 5};

    // Declaration and initialization of a character array (string)
    char arr2[] = "Hello";

    // Print the elements of the integer array
    printf("Elements of arr1: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");

    // Print the characters of the character array
    printf("Characters of arr2: ");
    for (int i = 0; arr2[i] != '\0'; i++) {
        printf("%c ", arr2[i]);
    }
    printf("\n");

    return 0;
}