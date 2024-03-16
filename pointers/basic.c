#include <stdio.h>

int main() {
    int x = 10;
    int *ptr; // Pointer declaration

    ptr = &x; // Pointer initialization with address of x

    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", &x);
    printf("Value stored at ptr: %d\n", *ptr); // Dereferencing pointer to access value
    printf("Address stored in ptr: %p\n", ptr);

    return 0;
}