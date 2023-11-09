import calendar

# Input year and month
year = int(input("Enter year (e.g., 2023): "))
month = int(input("Enter month (1-12): "))

# Create a calendar object
cal = calendar.month(year, month)

# Print the calendar
print(cal)
