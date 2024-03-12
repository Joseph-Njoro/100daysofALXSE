import datetime
import os

def get_last_log_date(log_file_path):
    """Get the date of the last log entry from the log file."""
    if os.path.getsize(log_file_path) == 0:
        return None  # Return None if the file is empty

    with open(log_file_path, "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()  # Get the last line
            try:
                last_date_str = last_line.split(":")[0]
                last_date = datetime.datetime.strptime(last_date_str, "%A %d %B %Y, %I:%M %p").date()
                return last_date
            except (ValueError, IndexError):
                pass
    return None

def main():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    start_date = datetime.date(2024, 3, 13)
    day_number = (current_date - start_date).days + 1
    days_remaining = 100 - day_number

    # Generate progress message
    progress_message = f"{current_datetime.strftime('%A %d %B %Y, %I:%M %p')}: Day {day_number} of 100: {days_remaining} more to go\n"

    # Define log file path
    log_file_path = "multiple_entries_log.txt"

    # Redudancy check
    last_date = get_last_log_date(log_file_path)
    if last_date == current_date:
        # If log entry for current date already exists, exit
        exit()

    # Write progress message to log file
    with open(log_file_path, "a") as file:
        file.write(progress_message)

    print(f"\033[1m\033[4m{progress_message}\033[0m")

if __name__ == "__main__":
    main()