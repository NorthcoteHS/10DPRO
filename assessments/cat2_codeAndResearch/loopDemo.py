"""
Prog:   loopDemo
Name:   Mr. Koopmans
Date:   10/05/18
Desc:   Demo of how to loop through two lists simultaneously.
"""

# Create lists of questions and answers.
questions = ['Is the sky blue?', 'How many legs does a chair have?', 'What is my name?']
answers = ['Yes', '4', 'Mr. Koopmans']

# Loop through each question *and* track the current index.
for i,item in enumerate(questions):
  # Display the question.
  print(item)

  # Use the current index (0, 1, 2, etc) to display the matching answer.
  print(answers[i])
