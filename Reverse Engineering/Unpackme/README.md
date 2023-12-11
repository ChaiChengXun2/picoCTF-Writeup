# Unpackme.py - CTF Challenge Writeup

Challenge: Unpackme.py
Points: 100
Category: Reverse Engineering

## Objective
The objective of the Unpackme.py challenge is to learn about reverse engineering in the context of Python programming. You will need to analyze the provided Python code to uncover a hidden flag.

## Solution
To successfully complete this challenge, follow these steps:

1. **Examine the Python file**: Start by examining the provided Python file. You may notice a weird encoded payload that resembles base64.

2. **Decode the payload**: Attempting to decode the payload may not yield the flag because it is not base64 encoding, at least from my testing. 

3. **Make the file executable**: To understand what the program does, you can make the Python file executable by running the following command:

        ```chmod +x <file>```

4. **Run the program**: After making the file executable, execute it to see what it does

5. **Try password guesses**: You can make password guesses, but in this case, the correct password may not be immediately apparent.

6. **Print plain**: Since you have access to the source code, try printing out the ```plain``` variable. This will reveal what the program does when the password is incorrect.

7. Review the program's output, and it will reveal the flag.

8. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discovered during the challenge.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Enjoy exploring Python reverse engineering, and happy hacking!
