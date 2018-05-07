# triviaGame

This is one of the available options for your CAT 2 Coding component.

## Description

You will create a quiz on a topic of your choosing. You can use multiple-choice, short-answer or any type of answer format you like.

Quizzes should let users know whether they got the answers correct, and display a score or other rating at the end.

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
- emulate your favourite game show's style of points/questions/gameplay
- incorporate difficulty settings and/or a timer
- accept multiple correct answers to a question (such as "List as many US states as you can.")
- save a high-score or leaderboard that persists when re-running the program
    - **Note:** this requires learning about File I/O
- show images
    - **Note:** this requires using the [Pillow module](https://pillow.readthedocs.io/en/3.1.x/installation.html#basic-installation) and [this method](https://stackoverflow.com/a/5333261/4080966) or similar