# Hangman
_______________________________________
Hangman is a word game in which one player (in this case, your program) thinks of a word, and the other player (in this case, the user) has to keep guessing letters until all the letter within the word are guessed. Generally, the player only has a limited amount of incorrect letters they can guess, usually around 10.

## Steps
_____________________________
1. Always start by creating a new file in IDLE (Ctrl+n or Command+n).

    - Save the new file as `Hangman.py` in your 10DPRO directory.
2. Have your program select a word, for more of a challenge, make it select a word randomly!
3. Get the user's letter guess using `input`
    - What prompt will you use to get this input?
    - What will happen if the user types in anything but a single letter?
4. If the user guessed a letter that **is** in the word, show them the position and ask for another guess, otherwise take away a life
5. If the user guessed the word, tell them they won! otherwise display agame over message
6. Feel free to use the resources below to help

## Resources
___________________________
| Requirement | Resource |
|-------------|----------|
| User input  | [input command (Python official docs)](https://docs.python.org/3/library/functions.html#input)----[The input function (Hands-on Tutorial)](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html) |
| `in` keyword | [Find if string is in another string](https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method)
|Random Numbers|<ul><li>[Generate random integers between 0 and 9 (StackOverflow)](https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9)</li><li>[random.randint (Official docs)](https://docs.python.org/3/library/random.html#random.randint)</li><li>[More about random numbers (effbot)](http://effbot.org/pyfaq/how-do-i-generate-random-numbers-in-python.htm)</li></ul>
| If statements  | <ul><li>[Intro to if statements (Programiz)](https://www.programiz.com/python-programming/if-elif-else)</li><li>[If statements (Hands-On Tutorial)](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html)</li><li>[Control Flow (Official Tutorial)](https://docs.python.org/3/tutorial/controlflow.html)</li></ul> |
| While loops | [While loops summary](https://www.w3schools.com/python/python_while_loops.asp)
## Assessment
____________________________
| Level  | Expectation                                                                                                            |   |   |   |
|--------|------------------------------------------------------------------------------------------------------------------------|---|---|---|
| Bronze | The program chooses a word, and tells the user when they have guesses a letter in that word, hard coded words          |   |   |   |
| Silver | The program allows the user to keep guessing until they have run our of lives or guessed the entire word, random words |   |   |   |
| Gold   | The program prints out which order the letters are in and uses lists instead of integers for randomness                |   |   |   |
- **Note:** all code should be commented and you should have no redundant code

Submit a zip of your final code on MyNH.
