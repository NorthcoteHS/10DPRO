# naming

At a certain point, every programmer has to stop and give some thought to how they are naming and organising their files and variables. For 10MCOD, that time is now.

There is no "right" way to name things, but there are important conventions that serve a few purposes:
- Like comments, a good variable name can make your code more readable to yourself and others.
- Conventions can help distinguish different types of objects, e.g. Classes (upper-case) vs variables (lower-case).
- Some conventions are required - e.g. variables (and sometimes files) cannot have spaces in their names.

Your task is to fix the folder structure and file/variable naming of the files in this module, and to solve a few unfinished programs. This will also help you practice using Git and GitHub.

## Conventions

Use these conventions to fix the attached code:

#### File names

Should have *no spaces*, be short but descriptive, start with a lower-case letter, and each subsequent word should be capitalised. This is called [**camel case**](https://en.wikipedia.org/wiki/Camel_case), and allows each word to stand out for legibility. Make sure to include a file extension (`.py`), and use only letters and numbers in the name. Example:

```
myFileName.py
```

#### Variable names

Same convention as file names - short, descriptive, uses camel case, and only letters and numbers. Example:

```python
firstName = 'Bob'
```

#### Dates

Each country has its own standard for how to write dates, however there is one clear standard when it comes to programming: YYYY-MM-DD. In this class, all dates should be formatted this way.

Why? Because computers rely heavily on being able to sort information, and the format above (which lists information from broadest to most specific) will lexically sort. Think of it like writing a number: you write the most significant digit first (e.g. thousands, followed by hundreds, ones, tenths, etc.). Example:

```
Date: 2018-03-29
```

## Steps

1. Download the .zip folder from MyNH and save in your coding folder.
2. Extract the folder from the .zip.
3. Fix the folder structure of the files in `naming`.
    - In this case we don't want any folders. Move all files to the root level of `naming`.
4. Fix all file names and file extensions (to .py).
    - Don't change README.md!
5. Check each file's docstring and update any invalid fields.
    - Replace "Student Name" with your own name.
    - Adjust all dates to use YYYY-MM-DD format.
6. Complete the Debugging, Complete The Code, and Commenting programs that you find, and commit.
7. Find one file with poorly named variables, fix them, and commit.
8. When completely done, zip the folder and submit to MyNH.
    - Remember to check the marking scheme for your progress.

## Marking Scheme

For each item on this list, you will receive one mark if it is completed correctly.

- [ ] All: files are located in the root directory
- [ ] All: file names are correctly formatted according to 10MCOD conventions
- [ ] All: files have correct extensions
- [ ] All: docstrings: Student's name has been added
- [ ] All: docstrings: Dates are in the correct format
- [ ] All: docstrings: Fields are updated based on changes made
- [ ] `Hello World! ^_^`: file appropriately renamed
- [ ] `New Text Document`: file appropriately renamed
- [ ] `asdf`: file appropriately renamed
- [ ] `asdf`: has proper variable names for the user’s name
- [ ] `asdf`: has proper variable names for the user’s date of birth
- [ ] `asdf`: has proper variable names for the user’s favourites
- [ ] `asdf`: Variable names are formatted according to 10MCOD conventions
- [ ] `debugMe`: File appropriately renamed
- [ ] `debugMe`: All typos corrected
- [ ] `debugMe`: Logic error corrected
- [ ] `debugMe`: All syntax errors corrected
- [ ] `debugMe`: All required packages imported 
- [ ] `debugMe`: Code runs free of errors
- [ ] `completeMe`: File appropriately renamed
- [ ] `completeMe`: Correct lines for getting length and width from user
- [ ] `completeMe`: Area is correctly calculated
- [ ] `completeMe`: Perimeter is correctly calculated
- [ ] `completeMe`: Perimeter is correctly displayed
- [ ] `completeMe`: Code runs free of errors
- [ ] `commentMe`: File appropriately renamed
- [ ] `commentMe`: complete docstring has been added
- [ ] `commentMe`: first section (print statement) has an appropriate comment
- [ ] `commentMe`: second section (r =) have appropriate comments
- [ ] `commentMe`: third section (area) has appropriate comments
- [ ] `commentMe`: fourth section (perimeter) has appropriate comments

Total: 31 Marks