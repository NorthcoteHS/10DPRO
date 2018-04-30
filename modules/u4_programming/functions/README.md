# functions

In Unit 2 we began learning to program in Python. We learned a few basic commands, like `print()` and `input()`, that end with brackets and let us pass values to them inside the brackets. These commands that end with brackets are called **functions**.

You can think of functions as "black boxes" - you send them information, they *do something* with it, and send some information back out:

![Black box](./Blackbox3D.png "Black box")

There is nothing special about `print()` and `input()`, except that they are *built-in* functions. You can create your own functions that work the exact same way!

### Creating functions: `def`

The following code uses the `def` command to create a function called `hello()` that says "Hello, World!":

```python
def hello():
    print('Hello, World!')
```

Notice that the code above *creates* the function, but doesn't call it. If you run the code, it won't do anything! But once it's created, you can call a function by using its name:

```python
def hello():
    print('Hello, World!')

hello()
```

### Input and output

As the "black box" picture above indicates, a function can receive input variables, and can also send an output variable when it is finished:

```python
def add(x,y):
    # This function has two inputs (x and y) and outputs their sum.
    return x + y

z = add(3,4)    # z will get the value 7.
```

### Grok

For further learning, complete the Grok lessons on functions: [Grok Python: Functions](https://groklearning.com/learn/intro-python-2/functions/0/).

Good luck and have fun!

## Exercises

In **this** folder, create a new Python file named `functions.py`, and create the following functions:

1. `hooray()`: Prints "Hooray!" to the screen.
2. `subtract(x,y)`: Takes two numbers as input, and returns their difference.
3. `double(x)`: Takes one number as input, and returns the number times two.
4. `excited(word)`: Takes one string as input, and returns the string with an exclamation mark to the end.
5. `stringJoin(str1, str2)`: Takes two strings as input, and returns the two strings joined with a space between them.
6. `birthday(name)`: Prints "Happy birthday, [name]!" to the screen (using the inputted name). No return value.
