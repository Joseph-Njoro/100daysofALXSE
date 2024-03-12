import datetime
start_date = datetime.date(2024,3,13)
current_date = datetime.date.today()

day_number = (current_date - start_date).days + 1
days_remaining = 100 - day_number

day_name = current_date.strftime("%A ")
date_str = current_date.strftime("%d %B ")

print(f"{day_name}{date_str}: Day {day_number} of 100: {days_remaining} more to go")