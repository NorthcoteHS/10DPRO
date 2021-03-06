# cipher

A *cipher* is one of the most basic ways to encrypt data. Encryption hides the meaning of information so that only those who know how to decrypt it can use it. You use encryption every day: signing in to websites, accessing the school's wi-fi, paying for things online or at the store, etc. Encryption is also used to keep corporate, military and government secrets.

A cipher is used to disguise written information by encoding the text though a series of defined steps. There are many types of ciphers, but today we'll focus on one: a caesar cipher. A caesar cipher encodes each letter in a message by replacing it with one a fixed number of letters later in the alphabet.

**Example:** If I offset every letter by one, a becomes b, b becomes c, c becomes d, ... y becomes z, z becomes a. So "The enemy approaches from the west at 6 o'clock!" becomes "Uif fofnz bqqspbdift gspn uif xftu bu 7 p'dmpdl!".

Notice that spaces and punctuation are left as they appear in the original text. Digits are shifted by the same offset (ex. 0 becomes 1, 1 becomes 2, ... 9 becomes 0).

Your task is to create a program that will encode a message (input by the user) with a caesar cipher, like the example above. It should display the encoded message at the end. Go for gold: allow the user to set the offset.

## Steps

1. Always start by creating a new file in IDLE (Ctrl+n or Command+n).

    - Save the new file as `cipher.py` in your 10DPRO directory.

2. Use `input` to get the message from the user.

    - Remember to give the user instructions

3. Use string operations to encode the message. You will need to understand the basics of ASCII - A computer uses ASCII codes to keep track of letters. Each character corresponds to a number (a = 97, b = 98, c = 99, etc. A = 65, B = 66, C = 67 etc.). See resources for details.

    - Start simple: Create an empty string, and make a for loop to read the input string one character at a time and add it to the end of the empty string.
        - This should produce a string that is exactly the same as the original string.
    - Now try to "shift" each character up by one (a->b, b->c, etc) before adding it to the empty string.
        - To do this, you must first convert each character to its ASCII (number) value, increase that number by 1, and convert back to a character.
        - Read in the resources below to understand ASCII and how to convert between characters and ASCII codes.

4. Output the encoded message to the user.

5. Use the resources below to guide you through the process.

6. You're done the basic task! Now try adding features, for instance:

    - Move the "cipher" logic into its own function that receives a string as input and returns a string as output.
    - Add a "decode" option that lets you decode text that has been encoded already.
    - Let the user choose the number of characters to shift by.
    - Support "wrap-around", so that letters stay within the alphabet (e.g. x->y, y->z, z->a).
    - Implement a more advanced type of cipher.

## Resources

| Requirement | Resource |
|-------------|----------|
| ASCII | <ul><li>[ASCII Alphabet Table](http://www.kerryr.net/pioneers/ascii2.htm)</li><li>[the `ord` and `chr` functions](https://www.dotnetperls.com/ord-python)</li><li>[ASCII Table (Including Non-Alphabetic Characters)](http://www.asciitable.com/)</li></ul>
| String Operations | <ul><li>[string - Common string operations (Python official docs)](https://docs.python.org/3/library/string.html)</li><li>[Manipulating Strings - Module 4 (Grok)](https://groklearning.com/learn/intro-python-1/manipulating-strings/0/)</li></ul> |
| For loops      | <ul><li>[For loops (W3Schools)](https://www.w3schools.com/python/python_for_loops.asp)</li><li>[Looping through each character in a string (StackOverflow)](https://stackoverflow.com/a/538374/4080966)</li></ul> |

## Extensions

- Try creating a decoder - input a message in code and use the program to determine the original message. Much harder if you don't know the offset!

- Research another type of cipher, such as a Vigenere or Rail Fence cipher. Create a program that endodes using that cipher

- If you are interested in Encryption and ciphers, research the Lorenz cipher and Enigma machine - used in Nazi Germany to send encoded messages. The Allies broke these codes at Blechley Park during World War II, which contributed greatly to the outcome of the war.

## Assessment

| Level  | Expectations |
|--------|--------------|
| Bronze   | Correctly substitutes letters with an offset of one, missing one or more silver feature (case-sensitivity, wrap-around or treatment of non-alphaetic characters) |
| Silver   | Correctly encodes message, including case-sensitivity, wrap-around (z becomes a) and treatment of non-alphabetic characters |
| Gold     | Correctly encodes message, and allows the user to set the offset (beware of large offsets) |
| Diamond  | Implementing a more advanced type of cipher (try a Vigenere or Rail Fence Cipher) |

- **Note:** all code should be commented and you should have no redundant code

Submit a zip of your final code on MyNH.
