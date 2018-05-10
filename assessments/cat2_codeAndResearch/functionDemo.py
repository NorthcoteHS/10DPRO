"""
Prog:   functionDemo
Name:   Mr. Koopmans
Date:   10/05/18
Desc:   Demo of how to use a function from *within* a for loop.
        Note that the function ("action") only deals with its own internal variables,
        "msg" and "response", which do not exist anywhere outside of the function.
"""

# Define a function that will display a message and return the response.
def action(msg):
    response = input(msg)
    return response

# Create a list of messages to display.
messages = ['Good morning! ', "G'day! ", 'Howdy! ']

# Loop through each message.
for message in messages:
    # Perform the action, and use the action's return value.
    answer = action(message)
    print('You said:', answer)
