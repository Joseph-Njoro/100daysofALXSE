#include <stdio.h>

// Define a struct for storing student information
struct Student {
    int id;
    char name[50];
    float gpa;
};

// Define a union for storing different types of data
union Data {
    int integer;
    float floating_point;
    char character;
};

int main() {
    // Create a struct instance and initialize its values
    struct Student student1;
    student1.id = 101;
    sprintf(student1.name, "John Doe");
    student1.gpa = 3.75;

    // Print student information using struct
    printf("Student ID: %d\n", student1.id);
    printf("Student Name: %s\n", student1.name);
    printf("Student GPA: %.2f\n\n", student1.gpa);

    // Create a union instance and initialize its values
    union Data data;
    data.integer = 10;

    // Print union data as integer
    printf("Data as Integer: %d\n", data.integer);

    // Change union data type and print as float
    data.floating_point = 3.14;
    printf("Data as Float: %.2f\n", data.floating_point);

    // Change union data type again and print as character
    data.character = 'A';
    printf("Data as Character: %c\n", data.character);

    // Demonstrate memory overlap in union
    printf("Memory Overlap in Union:\n");
    printf("Integer: %d\n", data.integer);
    printf("Float: %.2f\n", data.floating_point);
    printf("Character: %c\n", data.character);

    return 0;
}