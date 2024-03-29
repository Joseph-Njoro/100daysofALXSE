#include <stdio.h>

struct Person {
    char name[50];
    int age;
    union Contact {
        char email[50];
        char phone[15];
    } contact;
};

int main() {
    struct Person person1 = {"John", 25, {.email = "john@example.com"}};
    printf("Name: %\nAge: %dEmail: %s\n", person1.name, person1.age, person1.contact.email);
    return 0;
}