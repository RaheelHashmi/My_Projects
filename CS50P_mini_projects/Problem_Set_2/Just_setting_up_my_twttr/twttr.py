"""
When texting or tweeting, it’s not uncommon to shorten words to save time or 
space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str 
of text and then outputs that same text but with all vowels (A, E, I, O, and U) 
omitted, whether inputted in uppercase or lowercase.

Twitter ---------------> Twttr
What's your name? -----> Wht's yr nm?
CS50 ------------------> CS50
"""
user_input = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
filtered_input = []
for letter in user_input:
    if letter not in vowels:
        filtered_input.append(letter)
filtered_input = "".join(filtered_input)
print("Output:", filtered_input)
