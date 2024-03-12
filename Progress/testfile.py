import datetime

# Current date and time
current_datetime = datetime.datetime.now()
current_date = current_datetime.date()

# Define test file paths
empty_log_file = "empty_log.txt"
multiple_entries_log_file = "multiple_entries_log.txt"
invalid_dates_log_file = "invalid_dates_log.txt"

# Create empty log file
open(empty_log_file, "w").close()

# Create log file with multiple entries
with open(multiple_entries_log_file, "w") as file:
    file.write(f"{current_datetime.strftime('%A %d %B %Y, %I:%M %p')}: Day 1 of 100: 99 more to go\n")
    file.write(f"{current_datetime.strftime('%A %d %B %Y, %I:%M %p')}: Day 2 of 100: 98 more to go\n")
    file.write(f"{current_datetime.strftime('%A %d %B %Y, %I:%M %p')}: Day 3 of 100: 97 more to go\n")
    file.write(f"{current_datetime.strftime('%A %d %B %Y, %I:%M %p')}: Day 4 of 100: 96 more to go\n")
    file.write(f"{current_datetime.strftime('%A %d %B %Y, %I:%M %p')}: Day 4 of 100: 96 more to go\n")  # Duplicate entry for current date

# Create log file with invalid dates
with open(invalid_dates_log_file, "w") as file:
    file.write("Invalid Date Format: Day 1 of 100: 99 more to go\n")
    file.write("Invalid Date Format: Day 2 of 100: 98 more to go\n")
    file.write("Invalid Date Format: Day 3 of 100: 97 more to go\n")

print("Test files generated successfully.")