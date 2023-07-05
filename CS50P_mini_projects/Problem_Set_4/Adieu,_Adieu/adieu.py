"""
In The Sound of Music, there’s a song sung largely in English, So Long, 
Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be 
written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, 
one per line, until the user inputs control-z + enter. Assume that the user will 
input at least one name. Then bid adieu to those names, separating two names 
with one and, three names with two commas and one and, and n names with n-1 
commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

Here’s how to test your code manually:

Run your program with python adieu.py. Type Liesl and press Enter, followed by 
control-z + enter. Your program should output:
Adieu, adieu, to Liesl 

Run your program with python adieu.py. Type Liesl and press Enter, then type 
Friedrich and press Enter, followed by control-z + enter. Your program should 
output:
Adieu, adieu, to Liesl and Friedrich

Run your program with python adieu.py. Type Liesl and press Enter, then type 
Friedrich and press Enter. Now type Louisa and press Enter, followed by 
control-z + enter. Your program should output:
Adieu, adieu, to Liesl, Friedrich, and Louisa
"""
import inflect

names = []
while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:
        break

p = inflect.engine()
if len(names) == 2:
    print(f"Adieu, adieu, to {p.join(names, final_sep='')}")
else:
    print(f"Adieu, adieu, to {p.join(names)}")
