# [**Tip Calculator**](https://cs50.harvard.edu/python/2022/psets/0/tip/)
  > And now for my Wizard tip calculator.
  > 
  > — Morty Seinfeld
</blockquote>

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

```py
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

Well, we’ve written <em>most</em> of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:


  * `dollars_to_float`, which should accept a `str` as input (formatted as `$##.##`, wherein each `#` is a decimal digit), remove the leading `$`, and return the amount as a `float`. For instance, given `$50.00` as input, it should return `50.0`.
  * `percent_to_float`, which should accept a `str` as input (formatted as `##%`, wherein each `#` is a decimal digit), remove the trailing `%`, and return the percentage as a `float`. For instance, given `15%` as input, it should return `0.15`.

Assume that the user will input values in the expected formats.

$50.00, 15% ---------> Leave $7.50

$100.00, 18% --------> Leave $18.00

$15.00, 25% ---------> Leave $3.75