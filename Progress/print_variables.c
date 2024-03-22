#include <stdio.h>
#include <stdioarg.h>

void print_numbers(int count, ...) {
    va_list args;
    va_start(args, count);

    for (int i = 0; i < count; i++) {
        printf("%d ", va_arg(args, int);
    }

    va_end(args);
    printf("/n");
}

int main() {
    print_numbers(3, 10, 20, 30);
    print_numbers(5, 1, 2, 3, 4, 5);
    return 0;
}