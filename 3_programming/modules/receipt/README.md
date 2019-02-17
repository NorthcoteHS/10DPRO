# receipt

Your task is to create a basic program to generate a receipt for products purchased. It should prompt the user to enter items and prices until they choose to quit. Each item and price should be saved in a list. At the end, print the items and prices as well as a total. Format this in a readable way.
#### Example:

```
    Please enter an item (or quit): avocado
    Price? 2
    Please enter an item (or quit): avocado
    Price? 2
    Please enter an item (or quit): avocado
    Price? 2
    Please enter an item (or quit): bread
    Price? 2.50
    Please enter an item (or quit): bananas
    Price? 1.50
    Please enter an item (or quit): yogurt
    Price? 4
    Please enter an item (or quit): hommus
    Price? 7
    Please enter an item (or quit): quit

    Thank you for shopping :)

    avocado             $2.00
    avocado             $2.00
    avocado             $2.00
    bread               $2.50
    bananas             $1.50
    yogurt              $4.00
    hommus              $7.00
                       ------
    Total              $21.00

    Please come again!
```

## Steps

1. Start by creating a new file in IDLE. Save the new file as `receipt.py` in your 10MCOD directory.

2. Use a while loop to receive inputs from the user. You will probably need a counter variable to index your lists.

3. Determine the total by adding the prices together - tricky! It needs to work no matter how many items the user has added to the list.

4. Output the formatted receipt.

5. Use the resources below to guide you through the process.

## Resources

| Requirement | Resource |
|-------------|----------|
| Lists | <ul><li>[Lists Python Documentation](https://docs.python.org/3/tutorial/datastructures.html)</li><li>The lists module on GitHub</li></ul> |
| Loops | <ul><li>[While loops (TutorialsPoint)](https://www.tutorialspoint.com/python/python_while_loop.htm)</li></ul> |

## Extensions

- Instead of creating a separate list for items and prices, try creating a list where each element is a list containing both the name of the item and the price (ex. [[bananas, 2.5], [yogurt, 4], [bread, 2]])
- Be diligent about your formatting. Make everything line up vertically. Include dollar signs and .00 after whole number prices. This may be tedious!
- allow the user to specify how many of the same item they are buying. ex:
    ```
    Please enter an item (or quit): avocado
    How many? 4
    Price? 2
    Please enter an item (or quit): bread
    How many? 1
    Price? 2.50
    Please enter an item (or quit): quit
    ```
    could look like this on the receipt:
    ```
    avocado 4 @ $2       $8.00
    bread 1 @ $2.50      $2.50
                        ------
    Total               $10.50
    ```


## Assessment

| Level  | Expectations |
|--------|--------------|
| Bronze   | Generates a list of numbers from user input, prints them and gives a total. |
| Silver   | Stores separate lists of items and numbers and presents a formatted receipt. |
| Gold     | Implements one or more of the challenges. |

- **Note:** all code should be commented and you should have no redundant code.
