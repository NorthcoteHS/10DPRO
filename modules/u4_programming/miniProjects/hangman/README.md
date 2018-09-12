# hangman

Your task is to create a hangman game. It should
1. Choose a random word or phrase from a predefined list.
2. Present the player with the blank letters they will need to fill in.
3. Ask the player to choose letters or solve the puzzle.
4. When the player guesses correctly, it should fill in the blanks. 
5. When the player chooses incorrectly, it should cause a strike.
6. The game is over when either:
    - the user has completed the whole word
    - the user hits the max number of strikes (say 5 or 6)

#### Example:

```
    Welcome to Hangman. Here's your word:
    
    ________
    
    Guess a letter or solve: e
    Boo! Strike 1
    
    Guess a letter or solve: a
    Horray!
    
    _____a__
    
    Guess a letter or solve: t
    Boo! Strike 2
    
    Guess a letter or solve: s
    Horray!
    
    _____a_s
    
    Guess a letter or solve: o
    Horray!
    
    _oo__a_s
    
    Guess a letter or solve: Koopmans
    Correct! Congratulations!
    You had 2 strikes.
    
    Play again? no
    See you next time!

```

## Steps

1. Start by creating a new file in IDLE. Save the new file as `hangman.py` in your 10MCOD directory.

2. Create a list of at least 10 words for your program to choose from.

3. Randomly select one of the words from the list to be the game word (hint: the random library (`import random`) has a tool for this)
    
4. Determine the length of the word and print the appropriate number of blanks (you could use * or _ to represent the blanks).

5. Create a loop for the guessing process. The logic here is tough - what conditions will end the game? What should happen if the user guesses correctly/incorrectly? There are many cases - it may be helpful to draw a flow chart before you start coding.

6. Figure out how to correctly substitute the letters into the blanks (ex. _____a__)

7. Use the resources below to guide you through the process.

## Resources

| Requirement | Resource |
|-------------|----------|
| Lists | <ul><li>[Lists Python Documentation](https://docs.python.org/3/tutorial/datastructures.html)</li><li>The lists module on GitHub</li><li>[Random item from a list](https://www.tutorialspoint.com/python3/number_choice.htm)</li></ul> |
| String Operations | <ul><li>[string - Common string operations (Python official docs)](https://docs.python.org/3/library/string.html)</li><li>[Manipulating Strings - Module 4 (Grok)](https://groklearning.com/learn/intro-python-1/manipulating-strings/0/)</li><li>`in` will be a useful tool (ex. `"m" in "Koopmans"` returns True)</li></ul> |
| Loops | <ul><li>[While loops (TutorialsPoint)](https://www.tutorialspoint.com/python/python_while_loop.htm)</li></ul> |

## Extensions

- Let a second player set the words, but clear the output so the first player won't see the word on the screen! Keep score.
- Allow for phrases with multiple words. Leave spaces between the blanks so the use knows how long each word is.
- Do something else creative!
    

## Assessment

| Level  | Expectations |
|--------|--------------|
| Bronze   | Chooses a random word and allows the user to guess letters. Keeps track of strikes. |
| Silver   | Allows user to guess answer early. Player loses if they earn too many strikes. Game is replayable |
| Gold     | Implements one or more of the challenges. |

- **Note:** all code should be commented and you should have no redundant code.
