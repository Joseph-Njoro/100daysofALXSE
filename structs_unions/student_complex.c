#include <stdio.h>

struct Student {
    int id;
    char name[50];
    float gpa;
};

union Data {
    int integer;
    float floating_point;
    char character;
};

int main() {

    struct Student student1;
    student1.id = 101;
    sprintf(student1.name, "John Doe");
    student1.gpa = 3.75;

    printf("Student ID: %d\n", student1.id);
    printf("Student Name: %s\n", student1.name);
    printf("Student GPA: %.2f\n\n", student1.gpa);

    union Data data;
    data.integer = 10;

    printf("Data as Integer: %d\n", data.integer);

    data.floating_point = 3.14;
    printf("Data as Float: %.2f\n", data.floating_point);

    data.character = 'A';
    printf("Data as Character: %c\n", data.character);


    printf("Memory Overlap in Union:\n");
    printf("Integer: %d\n", data.integer);
    printf("Float: %.2f\n", data.floating_point);
    printf("Character: %c\n", data.character);

    return 0;
}