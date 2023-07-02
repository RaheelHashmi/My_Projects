"""
One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, 
which offers a menu of entrees, per the dict below, wherein the value of each 
key is a price in dollars. In a file called taqueria.py, implement a program 
that enables a user to place an order, prompting them for items, one per line, 
until the user inputs control-z + enter (which is a common way of ending one’s 
input to a program). After each inputted item, display the total cost of all 
items inputted thus far, prefixed with a dollar sign ($) and formatted to two 
decimal places. Treat the user’s input case insensitively. Ignore any input that 
isn’t an item. Assume that every item on the menu will be titlecased.

Here’s how to test your code manually:

Run your program with python taqueria.py. Type Taco and press Enter, then type 
Taco again and press Enter. Your program should output:
Total: $6.00  
and continue prompting the user until they input control-z + enter.

Run your program with python taqueria.py. Type Baja Taco and press Enter, then 
type Tortilla Salad and press enter. Your program should output:
Total: $12.00
and continue prompting the user until they input control-z + enter.

Run your program with python taqueria.py. Type Burger and press Enter. Your 
program should reprompt the user.

Be sure to try other foods and vary the casing of your input. Your program 
should behave as expected, case-insensitively.
"""
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
total = 0
while True:
    try:
        item = input("Item: ").strip().title()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        break
