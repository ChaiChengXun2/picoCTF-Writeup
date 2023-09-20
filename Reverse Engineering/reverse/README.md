# Reverse - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering  
**Points:** 100

## Objective

The "Reverse" challenge serves as an opportunity to familiarize yourself with C program code and apply reverse engineering techniques to extract the hidden flag.

## Solution

To successfully complete the "Reverse" challenge, you have multiple approaches at your disposal. One of the most straightforward methods involves using the `strings` command available on Linux to extract readable strings from the binary. Here are the steps:

1. **Use the `strings` Command:**
   - Open your terminal or command prompt.
   - Navigate to the directory where the binary file (`ret`) is located.
   - Run the following command to extract strings from the binary:
     ```bash
     strings ret
     ```
   - This command will display a list of strings found within the binary.

2. **Scroll Through the List:**
   - After executing the `strings` command, scroll through the list of extracted strings to find the flag.
   - The flag will be in the format `picoCTF{XXXXXXX}`.

Alternatively, if you prefer a more detailed and structured approach, you can use Ghidra, a powerful reverse engineering tool.

3. **Use Ghidra:**
   - Download and install Ghidra on your machine if you haven't already.
   - Open Ghidra and create a new project.
   - Import the `ret` binary into your project.
   - Analyze the binary using Ghidra's tools to reverse engineer the code.
   - Look for any clues or functions that may lead you to the flag.
   - Once you've identified the flag, it will be in the format `picoCTF{XXXXXXX}`.

With one of these methods, you will be able to extract the hidden flag and successfully complete the "Reverse" challenge.

Flag: `picoCTF{XXXXXXX}`

**Challenge Accomplished**
