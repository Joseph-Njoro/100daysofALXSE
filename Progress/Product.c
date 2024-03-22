#include <stdio.h>
#include <stdarg.h>

double product_double(int count, ...) {
    va_list args;
    va_start(args, count);

    double product = 1.0;
    for (int i = 0; i < count; i++) {
        product *= va_arg(args, double);
    }

    va_end(args);
    return product;
}

int main() {
    printf("Product: %.2f\n" product_double(3, 2.5, 1.5, 3.0));
    printf("Product: %.2f\n", product_double(4, 0.5, 2.0, 1.5, 3.0));
    return 0;
}