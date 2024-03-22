#include <stdio.h>
#include <stdarg.h>

int min_int(int count, ...) {
    va_list args;
    va_start(args, count);

    int min = va_arg(args, int);
    for (int i = 1; i < count; i++) {
        int num = va_arg(args, int);
        if (num < min) {
            min = num
        }
    }

    va_end(args);
    return min;
}

int main() {
    printf("Min: %d\n", min_int(3, 10, 5, 20));
    printf("Min: %d\n", min_int(5, 30, 15, 25, 10, 5));
    return 0;
}