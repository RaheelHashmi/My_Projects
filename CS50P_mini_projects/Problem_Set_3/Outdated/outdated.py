"""
In the United States, dates are typically formatted in month-day-year order 
(MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad 
design. Dates in that format can’t be easily sorted because the date’s year 
comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 
1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that 
format are also ambiguous. Harvard was founded on September 8, 1636, but 
9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that 
prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, 
no matter the country, formatting years with four digits, months with two 
digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a 
date, anno Domini, in month-day-year order, formatted like 9/8/1636 or 
September 8, 1636, wherein the month in the latter might be any of the values 
in the list below.
Then output that same date in YYYY-MM-DD format. If the user’s input is not a 
valid date in either format, prompt the user again. Assume that every month has 
no more than 31 days; no need to validate whether a month has 28, 29, 30, or 
31 days.

Here’s how to test your code manually:

Run your program with python outdated.py. Type 9/8/1636 and press Enter. Your 
program should output:
1636-09-08

Run your program with python outdated.py. Type September 8, 1636 and press 
Enter. Your program should output:
1636-09-08

Run your program with python outdated.py. Type 23/6/1912 and press Enter. Your 
program should reprompt the user.

Run your program with python outdated.py. Type December 80, 1980 and press 
Enter. Your program should reprompt the user.
"""
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    user_input = input("Date: ").strip()
    year = user_input[-4:]
    if user_input[0].isalpha():
        user_input_list = user_input.split(" ")
        month = user_input_list[0]
        date = user_input_list[1].replace(",", "")
        date = int(date)
    else:
        user_input_list = user_input.split("/")
        month = user_input_list[0]
        date = user_input_list[1]
        date = int(date)
        month = int(month)
    if date <= 31:
        if month in months:
            month = months.index(month) + 1
            print(f"{year}-{month:02}-{date:02}")
            break
        elif month <= 12:
            print(f"{year}-{month:02}-{date:02}")
            break
