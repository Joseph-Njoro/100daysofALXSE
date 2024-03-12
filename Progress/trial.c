#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Function to get the current date and time
void getCurrentDateTime(char *dateTimeStr) {
    time_t t = time(NULL);
    struct tm *tm_info = localtime(&t);
    strftime(dateTimeStr, 100, "%A %d %B %Y, %I:%M %p", tm_info);
}

// Function to calculate the number of days passed since start_date
int calculateDayNumber(struct tm *start_date, struct tm *current_date) {
    int day_number =
        (int)difftime(mktime(current_date), mktime(start_date)) / (24 * 60 * 60); // Convert seconds to days
    return day_number;
}

int main() {
    char progress_message[256];

    // Define the start date of the challenge
    struct tm start_date = {0};
    start_date.tm_year = 2024 - 1900; // Year - 1900
    start_date.tm_mon = 3 - 1;         // Month (0 - 11, so we subtract 1)
    start_date.tm_mday = 13;           // Day

    // Get the current date
    time_t t = time(NULL);
    struct tm *tm_info = localtime(&t);

    // Calculate the number of days passed since the start date
    int day_number = calculateDayNumber(&start_date, tm_info);

    // If the challenge hasn't started yet, set day_number to -1
    if (day_number < 0) {
        day_number = -1;
    }

    int days_remaining = (day_number >= 0) ? (100 - day_number) : 100;

    char day_name[100];
    getCurrentDateTime(day_name);

    sprintf(progress_message, "%s: Day %d of 100: %d more to go\n", day_name,
            (day_number >= 0) ? day_number : 0, days_remaining);

    // Define the path to the progress log file
    const char *log_file_path = "progress_log.txt";

    // Open progress log file
    FILE *file = fopen(log_file_path, "a");
    if (file) {
        // Read last line from log file
        char last_line[256];
        while (fgets(last_line, sizeof(last_line), file) != NULL) {
            continue;
        }
        fclose(file);

        if (strlen(last_line) > 0) {
            struct tm last_date;
            if (sscanf(last_line, "%*s %d %*s %d %d, %*d:%*d", &last_date.tm_mday, &last_date.tm_mon, &last_date.tm_year) == 3) {
                if (last_date.tm_mday == start_date.tm_mday &&
                    last_date.tm_mon == start_date.tm_mon &&
                    last_date.tm_year == start_date.tm_year) {
                    // If the log for the current day already exists, exit the program
                    exit(0);
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

    // Print progress message
    printf("%s", progress_message);

    return 0;
}