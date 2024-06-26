#include <stdio.h>
#include <string.h>

void reverseString(char *str) {
    int left = 0;
    int right = strlen(str) - 1;
    while (left < right) {
        char temp = str[left];
        str[left++] = str[right];
        str[right--] = temp;
    }
}

int main() {
    char str[] = "hello";
    printf("Original string: %s\n", str);
    reverseString(str);
    printf("Reversed string: %s\n", str);
    return 0;
}