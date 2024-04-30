#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random password
void generatePassword(int length, char* password) {
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}[]|\\;:'\"<>,.?/";

    srand((unsigned int)time(NULL));

    for (int i = 0; i < length; ++i) {
        int index = rand() % (sizeof(charset) - 1);
        password[i] = charset[index];
    }

    password[length] = '\0';
}

int main() {
    int length;
    printf("Enter the length of the password: ");
    scanf("%d", &length);

    if (length <= 0) {
        printf("Invalid length. Please enter a positive integer.\n");
        return 1;
    }

    char password[length + 1];
    generatePassword(length, password);

    printf("Generated Password: %s\n", password);

    return 0;
}