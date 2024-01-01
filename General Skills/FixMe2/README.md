# FixMe2.py - CTF Challenge Writeup

Challenge: FixMe2.py
Points: 100
Category: General Skills

## Objective
The objective of the FixMe2.py challenge is to learn the basics of Python and correct errors in a Python program to uncover the hidden flag.

## Solution
To successfully complete this challenge, follow these methods:

**Method 1: Direct Hex Decoding**
1. **Examine the Python code**: Begin by examining the provided Python code. As in the previous challenge (FixMe1.py), you will find the flag encoded in hexadecimal.

2. **Decode the flag**: You can directly decode the hexadecimal flag to reveal the actual flag.

3. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discover during the challenge.

**Method 2: Correcting Syntax Errors**
1. **Identify the error**: The error in the Python code is on line 22: `if flag = ""`. This line attempts to compare the value of `flag` with an empty string. However, a single equals sign `=` is used instead of the double equals sign `==`, which is the correct syntax for equality comparison in Python.

2. **Correct the error**: To fix the error, modify the line so that it reads: `if flag == ""`. This ensures that the comparison is performed correctly.

3. When you open the file in a text editor with syntax highlighting, this error should be apparent, often highlighted in red.

4. **Flag revealed**: Once you've corrected the syntax error, you can run the Python program without encountering errors, and the flag will be printed.

5. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discover during the challenge.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Enjoy learning Python and solving code issues, and happy hacking!
