# studyBuddy

This is one of the available options for your CAT 2 Coding component.

## Description

For the Study Buddy, you will create a program that quizzes you on the school subject of your choice, with the aim to help you and others study for an upcoming test/exam. You can think of it as virtual "flash cards". These questions will likely take the form of:

- multiple choice questions, asking for A/B/C/D responses; or
- short-answer questions, comparing the input against the correct answer

After each question, users should get feedback about whether they were right or wrong, before being asked the next question. At the end they will be told how many questions total they got right.

## Assessment

Your program must use:

- at least one function
- at least one list
- at least one for loop
    - **Note:** Certain "Extension" options may remove the need of a for loop.

Your program will be assessed against [this rubric](../codingRubric.pdf). Note that some extension options (for "Above Level") are listed at the bottom of this page.

## Getting Started

Here's a basic structure ("algorithm") to get you started on your program:

1. Create a list of all your questions.
2. Create a second list of all your correct answers.
3. Use a for loop to go through each question in your list.
4. Within the for loop, call a function with the question and answer as inputs.
    - The function will ask the question, tell the user if their answer is correct, and return 1 or 0 indicating a correct or incorrect answer.
5. Tally the user's score and report it when the for loop has finished.

## Extension

To further improve your project, you may want to:

- ask questions in a random order
- present multiple-choice answers in a random order
- improve multiple-choice detection by ignoring case (A/a) and whitespace (`'a '`)
- improve short-answer detection by ignoring uppercase letters, articles ('the', 'a'), etc.
- in your code, combine questions and answers into a single "multi-dimensional" array
- randomly generate questions and compute the correct answers (e.g. for maths questions)
- save a high-score or leaderboard that persists when re-running the program
    - **Note:** this requires learning about File I/O
- show images with each question (e.g. a map for Geography, a cell diagram for Biology, etc.)
    - **Note:** this requires using the [Pillow module](https://pillow.readthedocs.io/en/3.1.x/installation.html#basic-installation) and [this method](https://stackoverflow.com/a/5333261/4080966) or similar
