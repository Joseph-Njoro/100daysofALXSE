#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isPalindrome(char str[], int start, int end) {
    if (start >= end) {
        return true; // Base case: Empty string or single character is always a palindrome
    }
    if (str[start] != str[end]) {
        return false; // If characters at start and end indices don't match, it's not a palindrome
    }
    return isPalindrome(str, start + 1, end - 1); // Check recursively for the inner substring
}

int main() {
    char str[] = "racecar";
    if (isPalindrome(str, 0, strlen(str) - 1)) {
        printf("%s is a palindrome\n", str);
    } else {
        printf("%s is not a palindrome\n", str);
    }
    return 0;
}