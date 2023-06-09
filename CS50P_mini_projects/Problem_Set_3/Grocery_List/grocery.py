"""
Suppose that you’re in the habit of making a list of items you need from the 
grocery store.

In a file called grocery.py, implement a program that prompts the user for 
items, one per line, until the user inputs control-z + enter (which is a common 
way of ending one’s input to a program). Then output the user’s grocery list in 
all uppercase, sorted alphabetically by item, prefixing each line with the 
number of times the user inputted that item. No need to pluralize the items. 
Treat the user’s input case-insensitively.

Here’s how to test your code manually:

Run your program with python grocery.py. Type mango and press Enter, then type 
strawberry and press Enter, followed by control-z + enter. Your program should 
output:
1 MANGO
1 STRAWBERRY

Run your program with python grocery.py. Type milk and press Enter, then type 
milk again and press Enter, followed by control-z + enter. Your program should 
output:
2 MILK

Run your program with python grocery.py. Type tortilla and press Enter, then 
type sweet potato and press Enter, followed by control-z + enter. Your program 
should output:
1 SWEET POTATO
1 TORTILLA
"""
grocery_list = {}
while True:
    try:
        item = input().strip().upper()
        if not item:
            continue
        if item not in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1
    except EOFError:
        break
grocery_list = dict(sorted(grocery_list.items()))
for item, count in grocery_list.items():
    print(f"{count} {item}")
