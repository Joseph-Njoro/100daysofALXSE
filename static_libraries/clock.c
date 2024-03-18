#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifdef _WIN32
    #include <windows.h>
    #define sleep(x) Sleep(x * 1000)
#else
    #include <unistd.h>
#endif

void clear_screen() {
    system("clear || cls");
}

void display_clock(int hours, int minutes, int seconds) {
    clear_screen();
    printf("┌────────────┐\n");
    printf("│  %02d:%02d:%02d  │\n", hours, minutes, seconds);
    printf("└────────────┘\n");
}

int main() {
    int hours, minutes, seconds;

    while (1) {
        time_t now = time(NULL);
        struct tm *local_time = localtime(&now);
        hours = local_time->tm_hour;
        minutes = local_time->tm_min;
        seconds = local_time->tm_sec;
        display_clock(hours, minutes, seconds);
        sleep(1);
    }

    return 0;
}
