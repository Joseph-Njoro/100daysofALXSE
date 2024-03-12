#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Function to get the current date and time
void getCurrentDateTime(char *dateTimeStr) {
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    strftime(dateTimeStr, 100, "%A %d %B %Y, %I:%M %p", &tm);
}

// Function to calculate the number of days passed since start_date
int calculateDayNumber() {
    struct tm start_date = {0};
    start_date.tm_year = 2024 - 1900; // Year - 1900
    start_date.tm_mon = 3 - 1;         // Month (0 - 11, so we subtract 1)
    start_date.tm_mday = 13;           // Day

    time_t now = time(NULL);
    struct tm *current_date = localtime(&now);
    int day_number =
        (int)difftime(now, mktime(&start_date)) / (24 * 60 * 60) + 1; // Convert seconds to days
    return day_number;
}

/**
*CREATE A COPY IF YOU WISH TO POKE AROUND WITH THE CODE
*Function to parse date and time string
*I created this function. It is very straighforward.
*Change it and you fuck up evrything
*This function acts as a replacement for time headerfile
*/ 
int my_strptime(const char *buf, const char *format, struct tm *timeptr) {
    return sscanf(buf, format, &timeptr->tm_mday, &timeptr->tm_mon,
                  &timeptr->tm_year, &timeptr->tm_hour, &timeptr->tm_min);
}

int main() {
    char progress_message[256];
    int day_number = calculateDayNumber();
    int days_remaining = 100 - day_number;

    char day_name[100];
    getCurrentDateTime(day_name);

    sprintf(progress_message, "%s: Day %d of 100: %d more to go\n", day_name,
            day_number, days_remaining);

    // Define the path to the progress log file
    const char *log_file_path = "progress_log.txt";

    // Open progress log file
    FILE *file = fopen(log_file_path, "a");
    if (file) {
        // last line from log file
        char last_line[256];
        while (fgets(last_line, sizeof(last_line), file) != NULL) {
            continue;
        }
        fclose(file);

        if (strlen(last_line) > 0) {
            struct tm last_date;
            if (my_strptime(last_line, "%d %d %d, %d:%d", &last_date) == 5) {
                struct tm current_date;
                if (my_strptime(day_name, "%d %d %d, %d:%d", &current_date) == 5) {
                    if (last_date.tm_mday == current_date.tm_mday &&
                        last_date.tm_mon == current_date.tm_mon &&
                        last_date.tm_year == current_date.tm_year) {
                        // If the log for the current day already exists, exit the program
                        exit(0);
                    }
                }
            }
        }
    }

    // Append progress message to the log file
    file = fopen(log_file_path, "a");
    if (file) {
        fprintf(file, "%s", progress_message);
        fclose(file);
    }

    printf("\033[1m%s\033[0m", progress_message); // Bold

    return 0;
}