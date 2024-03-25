#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// ANSI escape codes for text styles and colors
#define ANSI_BOLD "\033[1m"
#define ANSI_RESET "\033[0m"
#define ANSI_COLOR_RED "\033[1;31m"
#define ANSI_COLOR_GREEN "\033[1;32m"

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

// Function to print border
void print_border(int width) {
    printf("╔");
    for (int i = 0; i < width; i++) {
        printf("═");
    }
    printf("╗\n");
}

int main() {
    srand(time(NULL)); // Seed for random number generation
    int target_number = generate_random_number(0, 255); // Generate random number between 0 and 255
    char bitwise_operator = generate_random_operator(); // Generate random bitwise operator
    int result = perform_bitwise_operation(target_number, bitwise_operator); // Perform bitwise operation
    int user_input;
    
    printf("\n");
    print_border(40); // Print top border

    printf("║" ANSI_BOLD " Welcome to the Bit Manipulation Challenge! " ANSI_RESET "║\n");
    printf("║ Target number: " ANSI_COLOR_RED "%d" ANSI_RESET "                    ║\n", target_number);
    printf("║ Apply the bitwise operator '%c' to the target number. ║\n", bitwise_operator);

    print_border(40); // Print middle border

    // Game loop
    while (1) {
        printf("║ Enter your answer: ");
        if (scanf("%d", &user_input) != 1) {
            printf("Invalid input! Please enter an integer.     ║\n");
            clear_input_buffer(); // Clear input buffer
            continue;
        }

        if (validate_input(user_input, result)) {
            printf("║" ANSI_COLOR_GREEN " Congratulations! You've correctly manipulated the number. " ANSI_RESET "║\n");
            break;
        } else {
            printf("║ Incorrect! Please try again.                    ║\n");
        }
    }

    print_border(40); // Print bottom border
    printf("\n");

    return 0;
}