#include <stdio.h>
#include <stdarg.h>
#include <time.h>

void custom_log(const char *format, ...) {
    va_list args;
    va_start(args, format);

    time_t rawtime;
    struct tm *timeinfo;
    time(&rawtime);
    timeinfo = localtime(rawtime);
    printf("[%02d:%02d:%02d] ", timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec);
    vprintf(format, args);

    va_end(args);
}

int main() {
    custom_log("Error: File not found!\n");
    custom_log("Warning: Resource consumption high!\n");
    return 0;
}