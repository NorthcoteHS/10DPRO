# personalityQuiz

This is one of the available options for your CAT 2 Coding component.

## Description

You will create a personality type quiz that puts the user into a category based on their answers to questions.

Examples:
- Which emoji are you?
- Which Hogwarts house do you belong in?
- A magazine style quiz (eg. "If you answered mostly As, you are easygoing and roll with the punches. Sometimes, you secretly wish you could get your way.")

Be creative with the types of questions you use, and use a calculation or comparison of some sort to assign the final result (it shouldn't be random).

The quiz should ask the series or questions, then output a final result based on the answers.

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
2. Create a second list to track the number of responses of each type (a/b/c etc). These counters should all start at 0.
3. Use a for loop to go through each question in your list.
4. Within the for loop, call a function with the question and answer as inputs.
    - The function will ask the question and return an indicator of which option was chosen (such as a number: 0 for a, 1 for b, 2 for c etc.)
5. Tally the number of responses of each type (a/b/c etc). When the loop has finished, determine the user's "personality" based on the result with the most responses, and display it to them.
    - **Note:** An alternative, instead of deciding based on the "most responses", is to generate a single score based on the responses - e.g. `a` is worth 1 point, `b` is worth 2, etc. This score can be tallied as you go, and the personality can be decided at the end based on ranges: 10-20 is one personality, 20-30 is another, etc.

## Extension

To further improve your project, you may want to:

- ask questions in a random order
- present multiple-choice answers in a random order
- improve multiple-choice detection by ignoring case (A/a) and whitespace (`'a '`)
- weight questions/answers based on how strongly they affect the user's final personality outcome
- ask different questions depending on previous answers
- show images with results
    - **Note:** this requires using the [Pillow module](https://pillow.readthedocs.io/en/3.1.x/installation.html#basic-installation) and [this method](https://stackoverflow.com/a/5333261/4080966) or similar