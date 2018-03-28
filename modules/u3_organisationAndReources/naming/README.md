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

1. Start by refreshing your personal repo with the latest commits from 10MCOD. In Brackets:
    - Open the Git extension, click the "origin" button near the right, and choose "upstream".
    - Hit the "Git Pull" button, which should show multiple available pulls.
    - When finished, return the first button to the "origin" setting.
2. From pulling, you will now have *this module* on your computer! Open the folder to view the files.
    - Use the "File Tree" on the left in Brackets to find `modules/u3/naming/`.
    - Right-click on the folder and choose "Show in Explorer".
3. Fix the folder structure of the files in `naming` and commit.
    - In this case we don't want any folders. Move all files to the root level of `naming`.
    - Remember to use a meaningful commit message.
4. Fix all file names and file extensions (to .py) and commit.
    - Don't change README.md!
5. Check each file's docstring and update any invalid fields, then commit.
    - Replace "Student Name" with your own name.
    - Adjust all dates to use YYYY-MM-DD format.
6. Complete the Debugging, Complete The Code, and Commenting programs that you find, and commit.
7. Find one file with poorly named variables, fix them, and commit.
8. When completely done, push your progress to GitHub!
    - Remember that you needed to  set your remote back to "origin" at the end of Step 1.
