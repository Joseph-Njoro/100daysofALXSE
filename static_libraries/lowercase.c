#include <ctype.h> // lowercase.c


void to_lowercase(char *str) {
    while (*str) {
        *str = tolower(*str);
        str++;
    }
}