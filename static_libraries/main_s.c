// main.c


#include <stdio.h>
#include "stringlib.h"

int main() {
    char str[] = "Hello, World!";
    
    printf("Original string: %s\n", str);
    
    to_uppercase(str);
    printf("Uppercase string: %s\n", str);
    
    to_lowercase(str);
    printf("Lowercase string: %s\n", str);
    
    printf("String length: %d\n", str_length(str));
    
    return 0;
}