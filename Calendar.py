""" import calendar
import datetime

# Get the current year
year = datetime.datetime.now().year

# Create an empty string for the combined calendar
combined_cal = ""

# Loop over each month of the year
for month in range(1, 13):
    # Create a calendar object
    cal = calendar.month(year, month)

    # Append the calendar to the combined calendar
    combined_cal += cal + "\n"

# Print the combined calendar
print(combined_cal)
 """
""" import calendar
import datetime
import tkinter as tk

# Get the current year
year = datetime.datetime.now().year

# Create an empty string for the combined calendar
combined_cal = ""

# Loop over each month of the year
for month in range(1, 13):
    # Create a calendar object
    cal = calendar.month(year, month)

    # Append the calendar to the combined calendar
    combined_cal += cal  + "\n"

# Create a root window
root = tk.Tk()

# Create a Text widget and insert the combined calendar
text = tk.Text(root)
text.insert(tk.END, combined_cal)
text.pack()

# Start the tkinter event loop
root.mainloop()
 """
""" 
import calendar
import datetime
import tkinter as tk

# Get the current year
year = datetime.datetime.now().year

# Create a root window
root = tk.Tk()

# Loop over each month of the year
for month in range(1, 13):
    # Create a calendar object
    cal = calendar.month(year, month)

    # Create a Text widget and insert the calendar
    text = tk.Text(root)
    text.insert(tk.END, cal)
    
    # Add the Text widget to the grid
    text.grid(row=0, column=month-1)

# Start the tkinter event loop
root.mainloop() """
""" 
import calendar
import datetime
import tkinter as tk

# Get the current year
year = datetime.datetime.now().year

# Create a root window
root = tk.Tk()

# Loop over each month of the year
for month in range(1, 13):
    # Create a calendar object
    cal = calendar.month(year, month)

    # Create a Text widget with minimal padding and border width, and insert the calendar
    text = tk.Text(root, padx=0, pady=0, borderwidth=0, highlightthickness=0)
    text.insert(tk.END, cal)

    # Add the Text widget to the grid
    text.grid(row=0, column=month-1)

# Start the tkinter event loop
root.mainloop() """

import calendar
import datetime
import tkinter as tk

# Get the current year
year = datetime.datetime.now().year

# Create a root window
root = tk.Tk()

# Loop over each month of the year
for month in range(1, 13):
    # Create a calendar object
    cal = calendar.month(year, month)

    # Create a Text widget with minimal padding, border width, and width, and insert the calendar
    text = tk.Text(root, padx=0, pady=0, borderwidth=0, highlightthickness=0, width=20)
    text.insert(tk.END, cal)

    # Add the Text widget to the grid
    text.grid(row=0, column=month-1)

# Start the tkinter event loop
root.mainloop()