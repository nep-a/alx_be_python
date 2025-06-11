import datetime 
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")
    number_of_days = int(input("Enter number of years to the current date: "))
    futur_date = datetime.datetime.now() + datetime.timedelta(days = number_of_days)
    print(f"Future date: {futur_date}")
display_current_datetime()