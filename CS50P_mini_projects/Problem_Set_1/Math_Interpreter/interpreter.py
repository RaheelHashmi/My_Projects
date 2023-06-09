"""
Python already supports math, whereby you can write code to add, subtract, 
multiply, or divide values and even variables. But let’s write a program that 
enables users to do math, even without knowing Python.

In a file called interpreter.py, implement a program that prompts the user for 
an arithmetic expression and then calculates and outputs the result as a 
floating-point value formatted to one decimal place. Assume that the user’s 
input will be formatted as x y z, with one space between x and y and one space 
between y and z, wherein:

1) x is an integer
2) y is +, -, *, or /
3) z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume 
that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your 
interpreter.py be an interpreter for math!

1 + 1  ------> 2.0
2 - 3  ------> -1.0
2 * 2  ------> 4.0
50 / 5 ------> 10.0
"""
operand1, operator, operand2 = input("Enter the operation: ").strip().split(" ")
operand1 = float(operand1)
operand2 = float(operand2)
match operator:
    case "+":
        answer = operand1 + operand2
    case "-":
        answer = operand1 - operand2
    case "*":
        answer = operand1 * operand2
    case "/":
        answer = operand1 / operand2
print(f"{answer: .1f}")
