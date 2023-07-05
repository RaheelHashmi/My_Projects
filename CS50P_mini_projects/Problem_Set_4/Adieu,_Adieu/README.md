# [**Adieu, Adieu**](https://cs50.harvard.edu/python/2022/psets/4/adieu/)
In [The Sound of Music](https://en.wikipedia.org/wiki/The_Sound_of_Music_(film)), there’s a song sung largely in English, [So Long, Farewell](https://www.youtube.com/watch?v=Qy9_lfjQopU), with these [lyrics](https://www.lyrics.com/lyric/3998488/Julie+Andrews/So+Long%2C+Farewell), wherein “adieu” means “goodbye” in French:

  > Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an [Oxford comma](https://en.wikipedia.org/wiki/Serial_comma)) as:

  > Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called `adieu.py`, implement a program that prompts the user for names, one per line, until the user inputs control-z + enter. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one `and`, three names with two commas and one `and`, and n names with n-1 commas and one `and`, as in the below:

  > Adieu, adieu, to Liesl<br>
  > Adieu, adieu, to Liesl and Friedrich<br>
  > Adieu, adieu, to Liesl, Friedrich, and Louisa<br>
  > Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt<br>
  > Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta<br>
  > Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta<br>
  > Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
 
Here’s how to test your code manually:

  * Run your program with `python adieu.py`. Type `Liesl` and press Enter, followed by control-z + enter. Your program should output:
    ```
    Adieu, adieu, to Liesl 
    ```
  * Run your program with `python adieu.py`. Type `Liesl` and press Enter, then type `Friedrich` and press Enter, followed by control-z + enter. Your program should output:
    ```
    Adieu, adieu, to Liesl and Friedrich
    ```
  * Run your program with `python adieu.py`. Type `Liesl` and press Enter, then type `Friedrich` and press Enter. Now type `Louisa` and press Enter, followed by control-z + enter. Your program should output:
    ```
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    ```
