# lists

We saw lists already in some of the modules of Unit 2, and even in App Inventor when you made your Magic 8-Ball (remember choosing a random response from a list?). We'll take some time now to talk about them a bit more formally.

In Python, a `list` is a variable that can have multiple items. For instance, imagine a shopping list with 6 items - we could write that as 6 separate variables:

```python
shopping1 = 'Eggs'
shopping2 = 'Bananas'
shopping3 = 'Yogurt'
shopping4 = 'Cereal'
shopping5 = 'Bread'
shopping6 = 'Pizza'
```

But it is much easier and more useful to combine all six strings into a single `list`:

```python
shopping = ['Eggs', 'Bananas', 'Yogurt', 'Cereal', 'Bread', 'Pizza']
```

### Creating lists: `[]`

A list is defined like any other variable (`name = value`), but to create the list we use square brackets and separate each list item with a comma:

```python
myList = [145, 'test', 3.14]
```

Notice that each item in the list can have any value - they do not all have to be strings (or numbers).

### Accessing items: `list[index]`

Lists are made up of multiple items. Often we want to use ("access") a single item from a list. For instance, we could print the first item of our shopping list from earlier:

```python
item1 = shopping[0]
print(item1)            # Will display 'Eggs'
```

Notice that we access a list item by using the list's name, followed by square brackets and a number. That number is called the *index*, and requires a bit more explanation.

#### The index

The index is the item number that we want to access from inside our list. The only trick is that the index *always counts from 0*. That means our first item is index 0, second item is 1, etc.

### Getting the length: `len(list)`

To get the length of a list (i.e. the number of items), use the `len()` function:

```python
nItems = len(shopping)
print(nItems)           # Will display '6'
```

### Adding items to a list: `list.append(item)`

To add a new item onto the *end* of a list, use the `.append()` method of your list:

```python
shopping.append('Ice cream')    # Becomes the 7th item
print(shopping[6])              # Will display 'Ice cream'
```

Note, this increases the length of your list by 1.

### Removing items from a list: `del list[index]`

To remove a specific item from a list, use `del` with the index to remove:

```python
del shopping[2]         # Removes the third item ('Yogurt')
print(shopping[2])      # Will display 'Cereal' (the new third item)
```

Note, this decreases the length of your list by 1.

### Changing items in a list

This can be done the same way as accessing the item, but then assigning it a new value:

```python
shopping[0] = 'Chocolate'
print(shopping[0])          # Will display 'Chocolate'
```

Now, as a result of all the changes we have made, our shopping list looks like:

```python
shopping = ['Chocolate', 'Bananas', 'Cereal', 'Bread', 'Pizza', 'Ice cream']
```


## Advanced usage

#### Negative index: `list[-ind]`

You can use a negative index to count backwards from the end of the list:

```python
lastItem = shopping[-1]
print(lastItem)             # Will display 'Ice cream'
```

Note that negative indices count from -1 (last item) downward, so the second-last would be -2, etc.

#### Accessing a range of items: `list[ind1:ind2]`

You can pull out a smaller "sub-list" of items from your list by using a colon in the index:

```python
first2 = list[0:2]      # Contains ['Chocolate', 'Bananas']
middle3 = list[1:4]     # Contains ['Bananas', 'Cereal', 'Bread']
```

Note that the second index needs to be 1 *greater than* the last item you want - e.g. `list[0:2]` only pulls out items 0 and 1.

There are even more advanced options that involve omitting the first or last index - this will take all values from the beginning (or to the end), using your other index:

```python
first3 = list[:3]       # Contains ['Chocolate', 'Bananas', 'Cereal']
last2 = list[-2:]       # Contains ['Pizza', 'Ice cream']
```

#### Other methods

There's plenty more that can be done with lists! Check out the [lists documentation](https://docs.python.org/3/tutorial/datastructures.html), [sorting](https://docs.python.org/3/howto/sorting.html), and more.

## Exercises

In **this** folder, create the files for the following exercises.

**Exercise 1:** Create a file called `classRoll.py`. In it, do the following:

1. Create the following list:
    `roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']`
2. Students take turns each week cleaning the class guinea pig cage. Print the name of the third student on the roll so they know it's their turn.
3. Create a variable called `enrolment` and assign it the number of students in the class (length of the list).
4. A new student arrived - `'James'`. Add him to the roll.
5. `'Jordan'` changed schools. Remove him from the roll.
6. `'Michael'` prefers to go by 'Mike'. Change his name on the roll.
7. (Challenge) Alphabetise the roll.
8. (Challenge) Reverse the list.
9. (Challenge) Print the name of a random student in the class.
10. (Challenge) Create two lists, each with 5 students (one with the first half of the class, the other with the second)


**Exercise 2:** Create a file called `userFaves.py`. In it, do the following:

1. Create an empty list called `favourites`.
2. While the user's input is not 'quit', ask the user for one of their favourite movies.
3. Each time they give a movie title, add the movie to the list.
4. At the end, thank them and tell them how many favourites they added to the list.
5. (Challenge) Within the loop, also ask for a rating and store it in a second list.
6. (Challenge) Rather than storing the movies and ratings as separate lists, instead store them together. To do this, make each pair its own list, and store it in a `favourites`. For example, `[['Shawshank Redemption', '10'], ['Jumanji', '8'], ['Frozen', '9']]`.
