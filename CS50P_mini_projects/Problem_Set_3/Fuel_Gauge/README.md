# [**Fuel Gauge**](https://cs50.harvard.edu/python/2022/psets/3/fuel/)
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called `fuel.py`, implement a program that prompts the user for a fraction, formatted as `X/Y`, wherein each of `X` and `Y` is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output `E` instead to indicate that the tank is essentially empty. And if 99% or more remains, output `F` instead to indicate that the tank is essentially full.

If, though, `X` or `Y` is not an integer, `X` is greater than `Y`, or `Y` is `0`, instead prompt the user again. (It is not necessary for `Y` to be `4`.) Be sure to catch any exceptions like [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) or [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).

3/4 -----------------> 75%

1/4 -----------------> 25%

4/4 -----------------> F

0/4 -----------------> E

4/0 -----------------> reprompt the user ([`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError))

three/four ---------> reprompt the user ([`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError))

1.5/3 ---------------> reprompt the user ([`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError))

5/4 -----------------> reprompt the user