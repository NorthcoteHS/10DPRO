# helloWorld

["Hello, World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) is the first program of almost every programmer. It is one of the most basic programs you can write, and simply displays the text "Hello, World!" to a screen (or other output).

Your task is to create a "Hello, World!" program in Python, then add a few extra features to make it more interesting!

## Steps

1. The starting interface of IDLE is called the "shell". Here you can type one-line commands that will be executed immediately.

    - Try typing: `print('Hello, world!')`

2. Instead of using the shell, we want to create a Python *file*. This lets us save a bunch of commands, and run them all together at once.

    - In IDLE, press Ctrl+n (Command+n on Mac) to create a new file. It will open in a separate window.
    - Save the new file right away with Ctrl+s, or `File -> Save`.
    - If you haven't already, **create a folder somewhere important** where you will save *all files and folders* related to this course. Call it `10MCOD` (or something similar).
    - Save this new file as `helloWorld.py` in your `10MCOD` folder (notice the extension - all Python files should end in `.py`).

3. Remember `print('Hello, World!')`? Write that as your program's first line, then save and run (F5, or `Run -> Run Module`).

4. Try modifying your code so that it outputs this message (with your name):
    ```
    Hello, World! My name is [your name].
    ```

5. Using the resources below, figure out how to ask the user their name, and incorporate it into your message:
    ```
    Hello, [user name]! My name is [your name].
    ```

6. Read about "comments" below, and add a docstring and block comments to your code.

## Resources

| Requirement | Resource |
|-------------|----------|
| User input  | <ul><li>[input command (Python official docs)](https://docs.python.org/3/library/functions.html#input)</li><li>[the input function (Hands-on Tutorial)](https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html)</li></ul> |
| Output      | <ul><li>[print command (Python official docs)](https://docs.python.org/3/library/functions.html#print)</li><li>[joining strings with print (StackOverflow)](https://stackoverflow.com/a/38897300)</li></ul> |
| Commenting  | <ul><li>[How to use comments in Python (Python For Beginners)](http://www.pythonforbeginners.com/comments/comments-in-python)</li><li>[Python docstrings (Python For Beginners)](http://www.pythonforbeginners.com/basics/python-docstrings/)</li><li>Official Python [comments](https://www.python.org/dev/peps/pep-0008/#comments) and [docstrings](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring) (Python.org)</li></ul> |


## Assessment

| Level  | Expectations |
|--------|--------------|
| Bronze | "Hello, World!" with programmer's name in the message |
| Silver | Uses `input` to ask for and print back the user's name |
| Gold   | Comments and docstring |

At the end of each day, submit a zip of your entire working directory (including this module) on MyNHS.
