import datetime
import os

start_date = datetime.date(2024, 3, 13)
current_date = datetime.date.today()
day_number = (current_date - start_date).days + 1
days_remaining = 100 - day_number

# Format current date
day_name = current_date.strftime("%A ")
date_str = current_date.strftime("%d %B ")

progress_message = f"{day_name}{date_str}: Day {day_number} of 100: {days_remaining} more to go\n"

# Define the path to the progress log file
log_file_path = "progress_log.txt"

# Redudancy check
if os.path.exists(log_file_path):
    with open(log_file_path, "r") as file:
        last_line = file.readlines()[-1]
    last_date = datetime.datetime.strptime(last_line.split(":")[0], "%A %d %B ")
    if last_date.date() == current_date:
        exit()

# Write progress message to the log file
with open(log_file_path, "a") as file:
    file.write(progress_message)
