# Patchme.py - CTF Challenge Writeup

Challenge: Patchme.py
Points: 100
Category: Reverse Engineering

## Objective
The objective of the Patchme.py challenge is to learn about reverse engineering in the context of Python programming. Your task is to analyze the provided Python code to discover the hidden flag.

## Solution
To successfully complete this challenge, follow these steps:

1. **Read the Python code**: Start by examining the provided Python code within the file.

2. **Multi-line check on the password**: As you go through the code, you will find a multi-line check on the password. This suggests that the flag is hidden within the code itself.

3. **Join the strings manually**: To reveal the flag, you need to manually join the strings that are part of the multi-line check. These strings, when combined, will form the flag.

4. **Run the Python file**: Once you have manually reconstructed the flag, run the Python file. This may involve using a Python interpreter or executing the code.

5. Input the strings you found as the password when prompted by the Python program.

6. If the strings you entered match the expected password, the program will provide you with the flag.

7. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discovered during the challenge.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Happy Python reverse engineering, and happy hacking!
