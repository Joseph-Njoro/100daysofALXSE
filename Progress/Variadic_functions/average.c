#include <stdio.h>
#include <stdarg.h>

float average(int count, ...) {
    va_list args;
    va_start(args, count);

    float total = 0.0;
    for (int i = 0; i < count; i++) {
        total += va_arg(args, double);
    }

    va_end(args);
    return total / count;
}

int main() {
    printf("Average: %.2f\n, average(4, 10.5, 20.3, 15.7, 8.2));
    printf("Average: %.2f\n", average(3, 2.5, 5.0, 7.5));
    return 0;
}