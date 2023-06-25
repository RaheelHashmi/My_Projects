"""
In deep.py, implement a program that prompts the user for the answer to the 
Great Question of Life, the Universe and Everything, outputting Yes if the user 
inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

42 -------------------> Yes
Forty Two ------------> Yes
forty-two ------------> Yes
50 -------------------> No

Be sure to vary the casing of your input and “accidentally” add spaces on either 
side of your input before pressing enter. Your program should behave as 
expected, case- and space-insensitively.
"""
QUESTION = "What is the Answer to the Great Question of Life, the  Universe, \
and Everything? "
answer = input(QUESTION).strip().lower()
match answer:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")
