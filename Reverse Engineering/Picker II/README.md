# Picker II - Reverse Engineering Challenge

## Basic Information
- **Name:** Picker II
- **Category:** Reverse Engineering
- **Points:** 100

## Objective
The "Picker II" challenge is designed to help participants learn reverse engineering in Python and exploit vulnerabilities in a Python program.

## Solution
To successfully complete the "Picker II" challenge, follow these steps:

1. **Analyze the Source Code:**
   - Begin by analyzing the provided Python source code.
   - Notice that the source code appears to be similar to the previous "Picker I" challenge.

2. **Identify Vulnerability:**
   - Typing "win" doesn't work this time, there is a hard-coded patch that has been applied to fix the previous vulnerability.
   - However, by examining the source code further, we discover an alternative way to obtain the flag.

3. **Flag Retrieval Method:**
   - Examine line 78 of the source code:
     ```
     flag = open('flag.txt', 'r').read()
     ```
   - This line reads the contents of the file `flag.txt` and stores it in the `flag` variable.

4. **Exploit the Vulnerability:**
   - To obtain the flag, you can mimic the behavior of the program and print the flag directly.
   - Use the following Python code to print the flag:
     ```python
     print(open('flag.txt', 'r').read())
     ```

## Flag
Congratulations! You have successfully solved the "Picker II" reverse engineering challenge. By understanding the source code and exploiting the flag retrieval method, you've uncovered the flag
