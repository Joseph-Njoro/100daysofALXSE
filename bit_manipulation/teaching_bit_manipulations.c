#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number between min and max (inclusive)
int generate_random_number(int min, int max) {
    return rand() % (max - min + 1) + min;
}

// Function to generate a random bitwise operator
char generate_random_operator() {
    char operators[] = {'<', '>', '~', '&', '|'}; // Bitwise operators
    int index = rand() % (sizeof(operators) / sizeof(operators[0])); // Random index
    return operators[index];
}

// Function to perform bitwise operation based on operator
int perform_bitwise_operation(int number, char operator) {
    switch (operator) {
        case '<':
            return number << 1;
        case '>':
            return number >> 1;
        case '~':
            return ~number;
        case '&':
            return number & 0xFF;
        case '|':
            return number | 0xFF;
        default:
            return number;
    }
}

// Function to validate user's input
int validate_input(int input, int target) {
    return input == target;
}

// Function to clear input buffer
void clear_input_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main() {
    srand(time(NULL)); // Seed for random number generation
    int target_number = generate_random_number(0, 255); // Generate random number between 0 and 255
    char bitwise_operator = generate_random_operator(); // Generate random bitwise operator
    int result = perform_bitwise_operation(target_number, bitwise_operator); // Perform bitwise operation
    int user_input;
    
    printf("Welcome to the Bit Manipulation Challenge!\n");
    printf("Your target number is: %d\n", target_number);
    printf("Apply the bitwise operator '%c' to the target number.\n", bitwise_operator);

    // Game loop
    while (1) {
        printf("Enter your answer: ");
        if (scanf("%d", &user_input) != 1) {
            printf("Invalid input! Please enter an integer.\n");
            clear_input_buffer(); // Clear input buffer
            continue;
        }

        if (validate_input(user_input, result)) {
            printf("Congratulations! You've correctly manipulated the number.\n");
            break;
        } else {
            printf("Incorrect! Please try again.\n");
        }
    }

    return 0;
}