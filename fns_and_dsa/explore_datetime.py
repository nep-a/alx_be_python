# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """Prompt the user to enter a number of days, then calculate and display the future date."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer number.")
        return

    future_date = datetime.now() + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if _name_ == "_main_":
    display_current_datetime()
    calculate_future_date()
