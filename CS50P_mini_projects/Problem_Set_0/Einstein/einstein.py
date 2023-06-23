"""
Even if you haven’t studied physics (recently or ever!), you might have heard 
that E = mc^2, wherein E represents energy (measured in Joules), m represents 
mass (measured in kilograms), and c represents the speed of light (measured 
approximately as 300000000 meters per second), per Albert Einstein et al. 
Essentially, the formula means that mass and energy are equivalent.

In a file called einstein.py, implement a program in Python that prompts the 
user for mass as an integer (in kilograms) and then outputs the equivalent 
number of Joules as an integer. Assume that the user will input an integer.

1 ---------> 90000000000000000
14 --------> 1260000000000000000
50 --------> 4500000000000000000
"""
def main():
    mass = int(input("m: "))
    energy = mass * (300000000 ** 2)
    print(f"E: {energy}")

main()