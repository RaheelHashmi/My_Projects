"""
I’m thinking of a number between 1 and 100…

What is it?
It’s 50! But what if it were more random?
In a file called game.py, implement a program that:

1) Prompts the user for a level, n. If the user does not input a positive 
integer, the program should prompt again.
2) Randomly generates an integer between 1 and n, inclusive, using the random 
module.
3) Prompts the user to guess that integer. If the guess is not a positive 
integer, the program should prompt the user again.

    a) If the guess is smaller than that integer, the program should output Too 
    small! and prompt the user again.
    b) If the guess is larger than that integer, the program should output 
    Too large! and prompt the user again.
    c) If the guess is the same as that integer, the program should output Just 
    right! and exit.

Here’s how to test your code manually:

Run your program with python game.py. Type cat at a prompt that says Level: and 
press Enter. Your program should reprompt you:
Level:

Run your program with python game.py. Type -1 at a prompt that says Level: and 
press Enter. Your program should reprompt you:
Level:

Run your program with python game.py. Type 10 at a prompt that says Level: and 
press Enter. Your program should now be ready to accept guesses:
Guess:   
Run your program with python game.py. Type 10 at a prompt that says Level: and 
press Enter. Then type cat. Your program should reprompt you:
Guess:   

Run your program with python game.py. Type 10 at a prompt that says Level: and 
press Enter. Then type -1. Your program should reprompt you:
Guess:   

Run your program with python game.py. Type 1 at a prompt that says Level: and 
press Enter. Then type 1. Your program should output:
Just right!  
There’s only one possible number the answer could be!

Run your program with python game.py. Type 10 at a prompt that says Level: and 
press Enter. Then type 100. Your program should output:
Too large!  
Looks like you’re guessing outside the range you specified.

Run your program with python game.py. Type 10000 at a prompt that says Level: 
and press Enter. Then type 1. Your program should output:
Too small!  
Most likely, anyways: you might get lucky and see Just right!. But it would 
certainly be odd for you to see Just right! every time. And certainly you 
shouldn’t see Too large!.
"""
import random

while True:
    level = input("Level: ").strip()
    if level.isdecimal() and int(level) > 0:
        level = int(level)
        number = random.randint(1, level)
        break
while True:
    guess = input("Guess: ").strip()
    if guess.isdecimal() and int(guess) > 0:
        guess = int(guess)
        if guess < number:
            print("Too small!")
            continue
        if guess > number:
            print("Too large!")
            continue
        print("Just right!")
        break
