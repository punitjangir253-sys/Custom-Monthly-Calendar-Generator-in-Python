from datetime import datetime

def display_month_calendar(year, month):
    # Names of the months and weekdays
    months = ["", "January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29

    # Print the Header
    print(f"\n   {months[month]} {year}".center(20))
    print("Mo Tu We Th Fr Sa Su")

    # Find the starting day of the week (0 = Monday, 6 = Sunday)
    start_day = datetime(year, month, 1).weekday()

    # Print initial spaces for the first week alignment
    print("   " * start_day, end="")

    # Loop through and print each day
    current_day = start_day
    for day in range(1, days_in_month[month] + 1):
        print(f"{day:2d} ", end="")
        current_day += 1
        
        # Break to a new line at the end of the week (Sunday)
        if current_day == 7:
            print()
            current_day = 0
    print("\n")

# --- Run the program directly by setting the values here ---
# Change these values to see different months/years without using input()
CHOSEN_YEAR = 2026
CHOSEN_MONTH = 9

display_month_calendar(CHOSEN_YEAR, CHOSEN_MONTH)
