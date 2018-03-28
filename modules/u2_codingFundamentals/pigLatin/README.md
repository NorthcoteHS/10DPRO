# pigLatin

Your task is to translate text (given by the user) to Pig Latin. Pig Latin is an argot (a secret language) that is formed by changing English words according to the following rules:
1. Words beginning with a vowel have the letters "ay" added to the end.
2. Words beginning with a consonent have all the letters before the first vowel moved to the end, then "ay" is added to the end.

Example: "Pig Latin is truly the language of intellectuals." translates to "igPay atinLay isay ulytray ethay anguagelay ofay intellectualsay."

Your program should be able to translate single words to Pig Latin. As an extension, try to have it translate full sentences!

## Steps

1. Always start by creating a new file in IDLE (Ctrl+n or Command+n).

    - Save the new file as `pigLatin.py` in your 10MCOD directory.

2. Use `input` to get the text from the user.

    - Remember to give the user instructions (eg. "Enter one word to translate: ")
    
3. Use `if` statements and string operations to translate the word.

    - Consider this: What will your program do if the user inputs a string with more than one word (eg. "Mario Kart")? It could...
        - Translate it to "ario KartMay" (this is a bronze-level solution)
        - Tell the user they've made a mistake, and ask them to retry
        - Translate all of the words in the string to Pig Latin (hard)
        - Something else...?

4. Output the result to the user. Remember to include some sort of message, like `Translation: `

5. Use the resources below to guide you through the process.

## Resources

| Requirement | Resource |
|-------------|----------|
| User input  | <ul><li>[input command (Python official docs)](https://docs.python.org/3/library/functions.html#input)</li><li>[the input function (Hands-on Tutorial)](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html)</li></ul> 
| If statements  | <ul><li>[Intro to if statements (Programiz)](https://www.programiz.com/python-programming/if-elif-else)</li><li>[If statements (Hands-On Tutorial)](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html)</li><li>[Control Flow (Official Tutorial)](https://docs.python.org/3/tutorial/controlflow.html)</li></ul> |
| String Operations | <ul><li>[string - Common string operations (Python official docs)](https://docs.python.org/3/library/string.html)</li><li>[Manipulating Strings - Module 4 (Grok)](https://groklearning.com/learn/intro-python-1/manipulating-strings/0/)</li></ul> |

## Assessment

| Level  | Expectations |
|--------|--------------|
| Bronze | Accurately chooses whether to move the first letter to the end, and adds the "ay" |
| Silver | Correctly translates words beginning with more than one consonent, and handles input of more than one word |
| Gold   | Correctly translates strings of more than one word |

- **Note:** all code should be commented and you should have no redundant code

At the end of each day, submit a zip of your entire working directory (including this module) on MyNHS.
