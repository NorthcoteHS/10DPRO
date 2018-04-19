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

### Grok

Your assignment is now to complete the Grok lessons on functions: [Grok Python: Functions](https://groklearning.com/learn/intro-python-2/functions/0/).

Good luck and have fun!
