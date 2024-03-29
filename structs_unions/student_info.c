#include <stdio.h>

struct Student {
    char name[50];
    int student_id;
    union Course {
        char major[50];
        char specialization[50];
    } course;
};

int main() {
    struct Student student1 = {"Alice", 101, {.major = "Computer Science"}};
    struct Student student2 = {"Bob", 102, {.specialization = "Data Science"}};

    printf("Student 1: Name = %s, Student ID = %d, Major = %s\n", student1.name, student1.student_id, student1.course.major);
    printf("Student 2: Name = %s, Student ID = %d, Specialization = %s\n", student2.name, student2.student_id, student2.course.specialization);

    return 0;
}