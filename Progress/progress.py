import datetime
import os

current_datetime = datetime.datetime.now()
start_date = datetime.date(2024, 3, 13)
day_number = (current_datetime.date() - start_date).days + 1
days_remaining = 100 - day_number

day_name = current_datetime.strftime("%A ")
date_str = current_datetime.strftime("%d %B %Y, %I:%M %p")

progress_message = f"{day_name}{date_str}: Day {day_number} of 100: {days_remaining} more to go\n"

# Define the path to the progress log file
log_file_path = "progress_log.txt"

# Redundancy check
if os.path.exists(log_file_path):
    with open(log_file_path, "r") as file:
        lines = file.readlines()
    if lines:
        last_line = lines[-1].strip()  # Remove leading/trailing whitespace
        if last_line:
            try:
                last_date_time = datetime.datetime.strptime(last_line.split(":")[0], "%A %d %B %Y, %I:%M %p")
                if last_date_time.date() == current_datetime.date():
                    # If the log for the current day already exists, exit the script
                    exit()
            except ValueError:
                # Handle invalid date format in the last line
                pass

# Write progress message to the log file
with open(log_file_path, "a") as file:
    file.write(progress_message)

# Print progress text using ANSI escape codes
print(f"\033[1m\033[4m{progress_message}\033[0m")