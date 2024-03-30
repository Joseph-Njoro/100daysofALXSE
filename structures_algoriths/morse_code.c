#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to translate text to Morse code
void textToMorse(char *text) {
    // Array to store Morse code equivalent of each character
    char *morseCode[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

    // Array of characters used for Morse code translation
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    printf("Morse Code: ");
    // Loop through each character in the input text
    for (int i = 0; text[i] != '\0'; i++) {
        // Convert uppercase characters to corresponding Morse code
        if (text[i] >= 'A' && text[i] <= 'Z') {
            printf("%s ", morseCode[text[i] - 'A']);
        }
        // Convert lowercase characters to corresponding Morse code
        else if (text[i] >= 'a' && text[i] <= 'z') {
            printf("%s ", morseCode[text[i] - 'a']);
        }
        // Print space for unknown characters
        else if (text[i] == ' ') {
            printf(" ");
        }
    }
    printf("\n");
}

// Function to translate Morse code to text
void morseToText(char *morse) {
    // Array to store Morse code equivalent of each character
    char *morseCode[] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

    // Array of characters used for Morse code translation
    char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Tokenize the input Morse code string based on spaces
    char *token = strtok(morse, " ");
    printf("Text: ");
    // Loop through each token
    while (token != NULL) {
        // Search for the token in the Morse code array and print the corresponding character
        for (int i = 0; i < 26; i++) {
            if (strcmp(token, morseCode[i]) == 0) {
                printf("%c", alphabet[i]);
                break;
            }
        }
        // Get the next token
        token = strtok(NULL, " ");
    }
    printf("\n");
}

int main() {
    char input[100];

    printf("Enter '1' to translate text to Morse code or '2' to translate Morse code to text: ");
    int choice;
    scanf("%d", &choice);

    // Clear input buffer
    while(getchar() != '\n');

    if (choice == 1) {
        printf("Enter text to translate to Morse code: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0; // Remove newline character
        textToMorse(input);
    } else if (choice == 2) {
        printf("Enter Morse code to translate to text (separate characters with spaces): ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0; // Remove newline character
        morseToText(input);
    } else {
        printf("Invalid choice. Please enter '1' or '2'.\n");
    }

    return 0;
}