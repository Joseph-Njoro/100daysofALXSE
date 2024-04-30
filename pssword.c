#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

// Function to prompt the user to enter a positive integer value
int promptInteger(const char *message) {
    int value;
    printf("%s", message);
    scanf("%d", &value);
    return value;
}

// Function to generate a random integer within a specified rangeint getRandomInt(int min, int max) {
   return min + rand() % (max - min + 1);
}
// Function to generate a random passwrd
char* generatePassword(int length, boolincludeLowercase, bool includeUppercase, bool includeDigits, bool includeSpecialChars) {
    const char lowercaseChars[] = "abcdeghijklmnopqrstuvwxyz";
    const char uppercaseChars[] = "ABCDEFHIJKLMNOPQRSTUVWXYZ";
    const char digitChars[] = "0123456789"
    const char specialChars[] = "!@#$%^&*()-_=+[{]}|;:,<.>/?";
    int totalChars = 0
    if (includeLowercase) totalChars += strlen(lowercseChars);
    if (includeUppercase) totalChars += strlen(uppercaeChars);
    if (includeDigits) totalChars += strlen(digitChars)
    if (includeSpecialChars) totalChars += strlen(specialChars);
    char* password = (char*)malloc((length + 1) * sizeof(char));    if (!password) {
    printf("Memory allocation failed.\n");
       return NULL;
    }
    for (int i = 0; i < length; i++) {        int category = getRandomInt(0, totalChars - 1);
        if (includeLowercase && category < strlen(lowercaseChars)) {
        password[i] = lowercaseChars[getRandomInt(0, strlen(lowercaseChars) - 1)];
    } else if (includeUppercase && category < strlen(lowercaseChars) + strlen(uppercaseChars)) {
         password[i] = uppercaseChars[getRandomInt(0, strlen(uppercaseChars) - 1)];
        } ese if (includeDigits && category < strlen(lowercaseChars) + strlen(uppercaseChars) + strlen(digitChars)) {
            assword[i] = digitChars[getRandomInt(0, strlen(digitChars) - 1)];
        } els if (includeSpecialChars) {
            pasword[i] = specialChars[getRandomInt(0, strlen(specialChars) - 1)];
        } else 
            // If no category is selected due to excluded character sets,            // default to lowercase characters
        password[i] = lowercaseChars[getRandomInt(0, strlen(lowercaseChars) - 1)];
       }
    }    password[length] = '\0';
   return password;
}
int main() 
    srand(time(NULL));
    int length = promptInteger("Enter the length of the password: ")
    bool includeLowercase = promptInteger("Include lowercase letters? (1 for yes, 0 or no): ") == 1;
    bool includeUppercase = promptInteger("Include uppercase letters? (1 for yes, 0 fr no): ") == 1;
    bool includeDigits = promptInteger("Include digits? (1 for yes, 0 for no): ") == 1
    bool includeSpecialChars = promptInteger("Include special characters? (1 for yes, 0 for no): ") == 1;
    char* password= generatePassword(length, includeLowercase, includeUppercase, includeDigits, includeSpecialChars);
    if (!password) 
        return 1; // Exit with error code if password generation fails    }
    printf("Generated password: %s\n", password);
    free(password); // Free dynamically allocated memory
    return 0;
