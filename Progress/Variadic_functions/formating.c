#include <stdio.h>
#include <stdarg.h>

void print_formatted_strings(const char format, ...) {
    va_list args;
    va_start(args, format);

    vprintf(format args);

    va_end(args);
}

int main() {
    print_formatted_strings("Welcome, %%s and %s!\n", "Alice", "Bob");
    print_formatted_strings("Today's weather forecast: %d%% chance of %s.\n", 80, "rain");
    return 0;
}