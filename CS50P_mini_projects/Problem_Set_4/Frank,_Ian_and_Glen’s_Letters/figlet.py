r"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 
1990s for making large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

1) Expects zero or two command-line arguments:

    a) Zero if the user would like to output text in a random font.
    b) Two if the user would like to output text in a specific font, in which 
    case the first of the two should be -f or --font, and the second of the two 
    should be the name of the font.

2) Prompts the user for a str of text.
3)Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or 
--font or the second is not the name of a font, the program should exit via 
sys.exit with an error message.

Here’s how to test your code manually:

Run your program with python figlet.py test. Your program should exit via 
sys.exit and print an error message:
Invalid usage

Run your program with python figlet.py -a slant. Your program should exit via 
sys.exit and print an error message:
Invalid usage

Run your program with python figlet.py -f invalid_font. Your program should exit 
via sys.exit and print an error message:
Invalid usage

Run your program with python figlet.py -f slant. Type CS50. Your program should 
print the following:
   ___________ __________ 
  / ____/ ___// ____/ __ \
 / /    \__ \/___ \/ / / /
/ /___ ___/ /___/ / /_/ / 
\____//____/_____/\____/  

Run your program with python figlet.py -f rectangles. Type Hello, world. Your 
program should print the following:
 _____     _ _                        _   _ 
|  |  |___| | |___      _ _ _ ___ ___| |_| |
|     | -_| | | . |_   | | | | . |  _| | . |
|__|__|___|_|_|___| |  |_____|___|_| |_|___|
                  |_|                       

Run your program with python figlet.py -f alphabet. Type Moo. Your program 
should print the following:
M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo                  
"""
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 3:
    try:
        if sys.argv[1] not in ["-f", "--font"]:
            raise ValueError
        if sys.argv[2] not in figlet.getFonts():
            raise ValueError
        user_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(f"Output:\n{figlet.renderText(user_input)}")
    except ValueError:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    user_input = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(f"Output:\n{figlet.renderText(user_input)}")

else:
    sys.exit("Invalid usage")
