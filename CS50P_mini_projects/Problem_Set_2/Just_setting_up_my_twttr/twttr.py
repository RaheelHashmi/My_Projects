"""
When texting or tweeting, it’s not uncommon to shorten words to save time or 
space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str 
of text and then outputs that same text but with all vowels (A, E, I, O, and U) 
omitted, whether inputted in uppercase or lowercase.

Here’s how to test your code manually:

Run your program with python twttr.py. Type Twitter and press Enter. Your 
program should output:
Twttr   

Run your program with python twttr.py. Type What's your name? and press Enter. 
Your program should output:
Wht's yr nm?

Run your program with python twttr.py. Type CS50 and press Enter. Your program 
should output
CS50
"""
user_input = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
filtered_input = []
for letter in user_input:
    if letter not in vowels:
        filtered_input.append(letter)
filtered_input = "".join(filtered_input)
print("Output:", filtered_input)
