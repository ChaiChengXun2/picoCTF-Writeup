# Picker III - Reverse Engineering Challenge

## Basic Information
- **Name:** Picker III
- **Category:** Reverse Engineering
- **Points:** 100

## Objective
The "Picker III" challenge aims to teach participants about reverse engineering in Python and identifying vulnerable code, particularly focusing on the concept of overwriting the Global Offset Table (GOT) in C programs.

## Solution
To successfully complete the "Picker III" challenge, follow these steps:

1. **Analyze the Source Code:**
   - Begin by analyzing the provided Python source code.
   - Note that this challenge is different from "Picker I" and "Picker II" in terms of the underlying mechanism.

2. **Understanding the Challenge:**
   - Run the instance provided, and you will have the ability to execute various functions.
   - Key functions include:
     - `print_table`: Lists all available functions.
     - `read_variable`: Reads a variable.
     - `write_variable`: Overwrites a variable (this is where the challenge lies).
   - When `read_variable` is executed with the name of a function, it prints the function's address, which hints at a GOT overwrite challenge.
   - This is basically a python implementation of overwriting GOT in C programs.

3. **Exploiting GOT Overwrite:**
   - To exploit the challenge, we can choose `write_variable` to overwrite a function in the "GOT".
   - Replace `getRandomNumber` with `win` in the GOT, effectively redirecting calls to `getRandomNumber` to the `win` function.
   - Now, when `getRandomNumber` is called, it will execute the `win` function.

4. **Retrieve the Flag:**
   - Execute `getRandomNumber` or any other function to trigger the overwritten GOT.
   - The program will execute the `win` function, which prints the flag.

## Flag
Congratulations! You have successfully solved the "Picker III" reverse engineering challenge. By identifying the vulnerable code related to GOT overwrite and strategically choosing the `write_variable` function, you've obtained the flag.
