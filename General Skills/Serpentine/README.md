# Serpentine - CTF Challenge Writeup

Challenge: Serpentine
Points: 100
Category: General Skills

## Objective
The objective of the Serpentine challenge is to learn about the basics of Python programming. Your task is to ensure that a Python program correctly prints the hidden flag.

## Solution
To successfully complete this challenge, follow these steps:

1. **Run the Python program**: Start by running the provided Python program. The script contains the logic necessary to reveal the flag.

2. After running the program, you may notice that the flag doesn't print to the console.

3. The reason the flag is not printed is that the `print_flag()` function within the script isn't called.

4. Your goal is to modify the code so that it calls the `print_flag()` function. You can add this function call anywhere within the flow of the program.

5. It doesn't matter where you place the function call, as long as it's executed within the program's logic.

6. Once you modify the code to call `print_flag()`, run the program again.

7. This time, the program will execute the function and print the flag to the console.

8. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discover when you successfully run the Python program.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Enjoy your exploration of Python programming and ensuring the correct execution of code, and happy hacking!
