#include <stdio.h>

// Function prototypes
int perform_AND(int a, int b);
int perform_OR(int a, int b);
int perform_XOR(int a, int b);
int validate_input(int bits);

// Function to perform AND operation on two bit patterns
int perform_AND(int a, int b) {
    return a & b;
}

// Function to perform OR operation on two bit patterns
int perform_OR(int a, int b) {
    return a | b;
}

// Function to perform XOR operation on two bit patterns
int perform_XOR(int a, int b) {
    return a ^ b;
}

// Function to validate input
int validate_input(int bits) {
    return (bits >= 0 && bits <= 15);
}

int main() {
    int target = 15;  // Target bit pattern to achieve
    int player1_bits, player2_bits;  // Bit patterns chosen by players

    printf("Welcome to the Bit Manipulation Game!\n");
    printf("The target bit pattern is: %d\n\n", target);

    // Game loop
    while (1) {
        // Player 1's turn
        printf("Player 1's turn:\n");
        printf("Enter your bit pattern (0-15): ");
        while (scanf("%d", &player1_bits) != 1 || player1_bits < 0 || player1_bits > 15) {
            // Clear the input buffer
            while (getchar() != '\n');
            printf("Invalid input! Please enter an integer between 0 and 15: ");
        }

        // Player 2's turn
        printf("Player 2's turn:\n");
        printf("Enter your bit pattern (0-15): ");
        while (scanf("%d", &player2_bits) != 1 || player2_bits < 0 || player2_bits > 15) {
            // Clear the input buffer
            while (getchar() != '\n');
            printf("Invalid input! Please enter an integer between 0 and 15: ");
        }

        // Check if any player has achieved the target pattern
        if (perform_AND(player1_bits, player2_bits) == target ||
            perform_OR(player1_bits, player2_bits) == target ||
            perform_XOR(player1_bits, player2_bits) == target) {
            printf("\nCongratulations! One of the players has achieved the target bit pattern (%d).\n", target);
            break;
        } else {
            printf("\nSorry, neither player has achieved the target bit pattern yet. Keep trying!\n\n");
        }
    }

    return 0;
}