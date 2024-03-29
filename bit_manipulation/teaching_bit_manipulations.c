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

    int terminal_width = 180; // Width of the terminal
    int padding = (terminal_width - 36) / 2; // Padding to center align the challenge

    printf("\n");
    print_border(terminal_width); // Print top border

    printf("║"); // Start border
    for (int i = 0; i < padding; i++) {
        printf(" ");
    }
    printf(ANSI_BOLD " BIT MANIPULATION CHALLENGE! " ANSI_RESET);
    for (int i = 0; i < padding; i++) {
        printf("  ");
    }
    printf("║\n");
    
    printf("║"); // Start border
    for (int i = 0; i < padding; i++) {
        printf(" ");
    }
    printf("║\n"); // Empty line for spacing

    printf("║"); // Start border
    for (int i = 0; i < padding; i++) {
        printf(" ");
    }
    printf("║\n"); // Empty line for spacing

    printf("║"); // Start border
    for (int i = 0; i < padding; i++) {
        printf(" ");
    }
    printf("║ Target number: " ANSI_COLOR_RED "%d" ANSI_RESET "                                                                                        ║\n", target_number);
    
    printf("║"); // Start border
    for (int i = 0; i < padding; i++) {
        printf(" ");
    }
    printf("║ Apply the bitwise operator '%c' to the target number:'%d'                                                 ║\n", bitwise_operator, target_number);

    printf("║"); // Start border
    for (int i = 0; i < padding; i++) {
        printf(" ");
    }
    printf("║\n"); // Empty line for spacing

    print_border(terminal_width); // Print bottom border

    // Game loop
    while (1) {
        printf("║ Enter your answer: ");
        if (scanf("%d", &user_input) != 1) {
            printf("NDWANZI PRO MAX: enter an integer.     ║\n");
            clear_input_buffer(); // Clear input buffer
            continue;
        }

        if (validate_input(user_input, result)) {
            printf("║" ANSI_COLOR_GREEN " Congratulations! wewe si NDWANZI. " ANSI_RESET "║\n");
            break;
        } else {
            printf("║ Incorrect! !!FAILURE >>BRAIN MISS1NG.!!                    ║\n");
        }
    }

    print_border(terminal_width); // Print bottom border
    printf("\n");

    return 0;
}