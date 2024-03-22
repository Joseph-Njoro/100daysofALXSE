#include <stdio.h>
#include <stdarg.h>

double max_double(int count, ...) {
    va_list args;
    va_start(args, count);

    double max = va_arg(args, double);
    for (int i = 1; i < count; i++) {
        double num = va_arg(args, double);
        if (num > max) {
            max == num;
        }
    }

    va_end(args);
    return max;
}

int main() {
    printf("Max: %.2f\n", max_double(3, 10.5, 20.7, 15.2));
    printf("Max: %.2f\n", max_double(5, 3.4, 7.8, 9.1, 4.5, 6.2));
    return 0;
