# forLoops

In Unit 2 we learned about [while loops](https://github.com/NorthcoteHS/10MCOD/tree/master/modules/u2_codingFundamentals/review#while-loops), which let you repeat a block of code over and over again, checking each time whether a condition is still true.

It can be *very* useful to repeat a block of code a specific number of times, and to have a counter telling us which loop number we're on. This can be done using while loops:

```python
# Print the numbers from 0 to 9 by looping.
counter = 0
while counter < 10:
    print(counter)
```

But there is another type of loop, the *for loop*, that is specifically designed for this purpose:

```python
# Print the numbers from 0 to 9 by looping.
for counter in range(0,10):
    print(counter)
```

### Using `range()`

In the example above, we used `range(0,10)` to tell Python to loop from the numbers 0 to 9. Notice that it only goes to 9, not 10 - for the same reasons that our while loop example only looped to 9.

In general, you can use `range()` to loop between any two numbers:

```python
# Loop from 5 to 7.
for i in range(5,8):
    print(i)    # Displays 5, 6, 7

# Loop from 0 to 4 (note, using just one value loops from 0 by default).
for i in range(5):
    print(i)    # Displays 0, 1, 2, 3, 4

# Loop from 1 to 7 in steps of 2.
for i in range(1,8,2):
    print(i)    # Displays 1, 3, 5, 7

# Loop from 10 to 1 in steps of -1 (counting down).
for i in range(10,0,-1):
    print(i)    # Displays 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Using arrays

For loops have another very powerful feature - they can loop through each value of a list:

```python
# Loop through each item in a list.
shopping = ['Eggs', 'Bananas', 'Yogurt', 'Cereal', 'Bread', 'Pizza']
for item in shopping:
    print(item)     # Displays Eggs, Bananas, Yogurt, ...
```

### Advanced usage

It is possible to loop through a list *and* have a counter (the index of the current list item) using the `enumerate()` function:

```python
shopping = ['Eggs', 'Bananas', 'Yogurt', 'Cereal', 'Bread', 'Pizza']
for i,item in enumerate(shopping):
    print('List item #', i)
    print(item)
```

## Exercises

In **this** folder, create the following files to complete the exercises:

**Exercise 1:** Create a file called `countdown.py`

This program should use a for loop to count down from 10 to 1, then print BLASTOFF! It should wait one second between printing each number. You will need to `import time` at the beginning of your program and use `time.sleep( seconds )` to have the program wait before proceeding.

**Exercise 2:** Create a file called `goodDog.py`

Create the list `dogs = ['Spot', 'Rex', 'Bob', 'Rufus']`. Use a for loop to loop through the list and print a statement calling each dog a good boy.

**Exercise 3:** Create a file called `squareNumbers.py`

This program will use a for loop for the numbers 1 - 10. Each number should be squared and the result added to a new list called `squares`. Print the list at the end of the file.
