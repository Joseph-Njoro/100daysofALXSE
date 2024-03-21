#include <stdio.h>
#include <stdlib.h>

// define a struct
typedef struct {
    int id;
    char name[20];
} person;

int main() {
    person *ptr;

    // allocate memory for 1 person