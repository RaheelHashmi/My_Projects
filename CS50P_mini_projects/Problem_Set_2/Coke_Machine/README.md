# [**Coke Machine**](https://cs50.harvard.edu/python/2022/psets/2/coke/)
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called `coke.py`, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

Here’s how to test your code manually:

  * Run your program with `python coke.py`. At your `Insert Coin: ` prompt, type `25` and press Enter. Your program should output:
    ```
    Amount Due: 25   
    ```
    and continue prompting the user for coins.
  * Run your program with `python coke.py`. At your `Insert Coin: ` prompt, type `10` and press Enter. Your program should output:
    ```
    Amount Due: 40
    ```
    and continue prompting the user for coins.
  * Run your program with `python coke.py`. At your `Insert Coin: ` prompt, type `5` and press Enter. Your program should output:
    ```
    Amount Due: 45
    ```
    and continue prompting the user for coins.
  * Run your program with `python coke.py`. At your `Insert Coin: ` prompt, type `30` and press Enter. Your program should output:
    ```
    Amount Due: 50
    ```
    because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.
  * Run your program with `python coke.py`. At your `Insert Coin: ` prompt, type `25` and press Enter, then type `25` again and press Enter. Your program should halt and display:
    ```
    Change Owed: 0
    ```
  * Run your program with `python coke.py`. At your `Insert Coin: ` prompt, type `25` and press Enter, then type `10` and press Enter. Type `25` again and press Enter, after which your program should halt and display:
    ```
    Change Owed: 10
    ```
    
