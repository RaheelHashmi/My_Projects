"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity 
license plate for your car, with your choice of letters and numbers instead of 
random ones. Among the requirements, though, are:

1) “All vanity plates must start with at least two letters.”
2) “… vanity plates may contain a maximum of 6 characters (letters or numbers) 
and a minimum of 2 characters.”
3) “Numbers cannot be used in the middle of a plate; they must come at the end. 
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be 
acceptable. The first number used cannot be a ‘0’.”
4) “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and 
then output Valid if meets all of the requirements or Invalid if it does not. 
Assume that any letters in the user’s input will be uppercase. Structure your 
program per the below, wherein is_valid returns True if s meets all requirements 
and False if it does not. Assume that s will be a str. You’re welcome to 
implement additional functions for is_valid to call (e.g., one function per 
requirement).

CS50 --------------> Valid
CS05 --------------> Invalid
CS50P -------------> Invalid
PI3.14 ------------> Invalid
H -----------------> Invalid
OUTATIME ----------> Invalid
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        first_condition(s)
        and second_condition(s)
        and third_condition(s)
        and fourth_condition(s)
    )


def first_condition(s):
    return s[:2].isalpha()


def second_condition(s):
    return 2 <= len(s) <= 6


def third_condition(s):
    for character in s:
        if character.isdecimal():
            return character != "0" and s[s.index(character) :].isdecimal()
    return False


def fourth_condition(s):
    return s.isalnum()


main()
