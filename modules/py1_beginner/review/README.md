# Module Review

At this point, you've had three weeks to get familiar with Python and programming in a text-based environment. The aim of this document is to review the programming concepts you've learned through the modules and Grok in a more formal manner.

## Functions

Functions are the basic building blocks of any programming language. They are how we give the computer a command - how we tell it to *do* something. There is a full list of Python built-in functions [here](https://docs.python.org/3/library/functions.html).

The Python function you're probably most familiar with is `print()`.

#### `print()`

[`print()`](https://docs.python.org/3/library/functions.html#print) is a function that takes one input and displays it to the screen. For instance, this code will display `Hello, World!` to the user:

```python
print('Hello, World!')
```

#### `input()`

[`input()`](https://docs.python.org/3/library/functions.html#input) is like a sibling to `print()`. It takes one input, which it displays to the screen, and then waits for the user to type a response (which it returns as an output). For instance, this code will display `Say something: ` to the user, wait for the user to type a response, and then store that response in a variable called `response`:

```python
response = input('Say something: ')
```

#### `int()`

[`int()`](https://docs.python.org/3/library/functions.html#int) converts text or decimal numbers into an integer (a whole number). This is especially useful in combination with `input()`, which always returns a string. For example, the code below converts a string to a number and does basic math with it:

```python
# After the line below, x has a value of 10.
x = int('5') * 2
```

#### `str()`

[`str()`](https://docs.python.org/3/library/functions.html#func-str) converts a number into a string (text). This is useful if you want to join multiple strings using `+`. For example, the code below displays the current value of `x`:

```python
x = 5
message = 'The value of x is ' + str(x) + '.'
print(message)
```

#### `len()`

[`len()`](https://docs.python.org/3/library/functions.html#len) gets the length of a string or list. It takes one input (the string/list) and returns one output (the length). For example, the code below gets the length of the string `'Hello, World!'`:

```python
# After the line below, x has a value of 13.
x = len('Hello, World!')
```

#### `chr()` and `ord()`

[`chr()`](https://docs.python.org/3/library/functions.html#chr) converts a number to its [ASCII character representation](https://www.asciitable.com/), and `ord()` converts a character back to its ASCII number. For example, the code below prints the character `G` in both its number and text form:

```python
# The letter G has an ASCII character code of 107.
print(chr(107))
print(ord('G'))
```

### Libraries

Often we want to do more complex tasks that aren't covered in the "built-in functions", like generate a random number or get the current date. For many of these tasks, there are existing "libraries" that we can use with the `import` statement.

Some of the libraries we've used are described below. For a complete list of libraries, see [here](https://docs.python.org/3/contents.html) (starting with "6. Text Processing Services").

#### `random`

[`random`](https://docs.python.org/3/library/random.html) gives access to a range of functions to generate random numbers. For example, the code below imports the `random` module and prints a random integer between 1 and 10:

```python
import random
print(random.randint(1,10))
```

## Variables

Variables are a necessary piece to almost any program. If functions are how we *do* something in a program, variables are how we *remember* things.

When you create a variable, you can think of it as creating a "box" in the computer's memory where it can store a single value. For example, the code below creates the variable `x` and stores the value `1` inside of it:

<img align="right" height="25px" src="./var1.png">

```python
x = 1
```

Programming variables are different from mathematical variables. They simply store a value, and that value can be changed. For instance, the following command would be impossible in math:

<img align="right" height="25px" style="margin-top: 15px" src="./var2.png">

```python
# Increase x by 1, and store it back into x.
x = x + 1
```

### Variable types

Variables can be numbers (int or float), strings (text), Booleans (True/False), or a number of other unique types. A full list of built-in types can be found [here](https://docs.python.org/3/library/stdtypes.html).

Python is a "dynamically typed" language, meaning that you don't have to define what kind of variable you're making when you create it. For instance, `x` can start as a number and change to a string:

```python
# The following lines of code are valid, and results in printing 'Bob'.
x = 5
x = 'Bob'
print(x)
```

### Lists

In Python, a [`list`](https://docs.python.org/3/library/stdtypes.html#lists) is a way of creating a collection of related values. This can be useful when you want to "loop over" a set of items. You can access each item using its "index", or position number. For example, the code below creates a list of cars and prints the first, third, and last cars:

```python
# Notice counting starts from 0, and -1 is a special index for "last".
cars = ['Lexus', 'Mazda', 'Toyota', 'Audi', 'Subaru', 'Porsche']
print(cars[0])
print(cars[2])
print(cars[-1])
```

## If statements

Another of the fundamental concepts in programming, an `if` statement lets you run a block of code *only if* a certain condition is met. For example, the code below will print `Yay!` if the number `x` is greater than 10:

```python
x = 1
if x > 10:
    print('Yay!')
elif x > 5:
    print('Almost there!')
else:
    print('Not quite!')
```

Note that each "block" of code is **indented** with four spaces, which tells Python that it is attached to the `if` statement above it. The statement `elif` is short for "else if", and essentially performs another if statement, but only if the first condition *wasn't* true. `else` will run if none of the previous conditions were true.

## While loops

A loop is a way of repeating a block of code multiple times. It is like an `if` statement - it has a condition that it checks, and it will only run its code if the condition is true. Unlike an `if`, it will keep running its block of code until the condition isn't true, checking each time it finishes. For example, the code below will print 1 to 9, then `Done!`:

```python
x = 1
while x < 10:
    print(x)
    x = x + 1
print('Done!')
```

Like `if` statements, notice that the block of code performed by the `while` statement is all indented with four spaces.

## Comments

Comments are a way of writing human-readable descriptions of your code, for yourself and anyone else who may read your code in the future. There are [three types of comments](https://www.python.org/dev/peps/pep-0008/#comments) in Python:

1. **Block:** Starts with a `#` on a new line, and describes the following block of code:

    ```python
    # Increase x by 1.
    x = x + 1
    ```

2. **Inline:** Like a block comment, starts with a `#` but on the *same line* as code (avoid using):

    ```python
    x = x + 1   # Increase x by 1.
    ```

3. **[Docstring](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring):** A multi-line comment that starts and ends with `"""`:

    ```python
    """
    Multi-line
    comment.
    """
    ```

See the [commenting module](../commenting/) for more information.
