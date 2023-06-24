"""
Some people have a habit of speaking rather quickly, and it’d be nice to slow 
them down, a la YouTube’s 0.75 playback speed, or even by having them pause 
between words.

In a file called playback.py, implement a program in Python that prompts the 
user for input and then outputs that same input, replacing each space with ... 
(i.e., three periods).

This is CS50 -------------------------------> This...is...CS50
This is our week on functions --------------> This...is...our...week...on...functions
Let's implement a function called hello ----> Let's...implement...a...function...called...hello
"""
print(input("Say something: ").replace(" ", "..."))
