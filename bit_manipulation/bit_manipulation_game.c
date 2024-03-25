#include <stdio.h>
#include <stdbool.h>

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

// Function to validate user input
bool validate_input(int bits) {
    return bits >= 0 && bits <= 15;
}

int main() {
    int target = 15;  // Target bit pattern to achieve
    int player1_bits, player2_bits;  // Bit patterns chosen by players

    printf("Welcome to the Bit Manipulation Game!\n");
    printf("The target bit pattern is: %d\n\n", target);

    // Game loop
    while (true) {
        // Player 1's turn
        printf("Player 1's turn:\n");
        do {
            printf("Enter your bit pattern (0-15): ");
            scanf("%d", &player1_bits);
            if (!validate_input(player1_bits)) {
                printf("Invalid input! Please enter a number between 0 and 15.\n");
            }
        } while (!validate_input(player1_bits));

        // Player 2's turn
        printf("Player 2's turn:\n");
        do {
            printf("Enter your bit pattern (0-15): ");
            scanf("%d", &player2_bits);
            if (!validate_input(player2_bits)) {
                printf("Invalid input! Please enter a number between 0 and 15.\n");
            }
        } while (!validate_input(player2_bits));

        // Check if any player has achieved the target patter
