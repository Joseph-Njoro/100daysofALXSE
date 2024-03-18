#include <ctype.h> //upercase.c

void to_uppercase(char *str) {
    while (*str) {
        *str = toupper(*str);
        str++;
    }
}