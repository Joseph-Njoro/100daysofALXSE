import datetime

import time

import schedule


# Set the graduation date

graduation_date = datetime.date(2024, 11, 1)


# Define a function to print the motivational message

def print_motivational_message():

    now = datetime.datetime.now()

    days_until_graduation = (graduation_date - now.date()).days

    motivational_messages = [

        "You got this!",

        "Keep pushing forward!",

        "Believe in yourself!",

        "You're almost there!",

        "Don't give up now!",

        "Stay focused and determined!",

        "You can do anything you set your mind to!",

        "Keep going, you're making progress!",

        "You're stronger than you think!",

        "You're capable of achieving great things!"

    ]

    print(f"There are {days_until_graduation} days until graduation.")

    print(motivational_messages[days_until_graduation % len(motivational_messages)])


# Schedule the function to run every day at 10 AM

schedule.every().day.at("10:00").do(print_motivational_message)


# Print the initial message

now = datetime.datetime.now()

days_until_graduation = (graduation_date - now.date()).days

print(f"There are {days_until_graduation} days until graduation.")

print(motivational_messages[0])


# Run the scheduler in an infinite loop

while True:

    schedule.run_pending()

    time.sleep(1)


# Print a final message

print("Congratulations! You've graduated"