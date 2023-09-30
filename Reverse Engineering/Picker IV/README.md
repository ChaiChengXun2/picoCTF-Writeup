# Picker IV - Reverse Engineering Challenge

## Basic Information
- **Name:** Picker IV
- **Category:** Reverse Engineering
- **Points:** 100

## Objective
The "Picker IV" challenge aims to test participants' ability to identify functions within a C binary file and determine the address of a specific function.

## Solution
To successfully complete the "Picker IV" challenge, follow these steps:

1. **Analyze the Challenge Environment:**
   - This challenge is significantly different from "Picker I," "Picker II," and "Picker III."
   - You are provided with a C program and its corresponding binary file.
   - The program will require you to input a hexadecimal address, and it will jump to that address.

2. **Identify the Address of the Win Function:**
   - Begin by running the C binary file in a debugger like GDB (GNU Debugger).
   - In GDB, execute the following command to list all functions and their corresponding addresses:
     ```
     info functions
     ```
   - This will display a list of functions within the binary, along with their memory addresses.
   - Look for the `win` function in the list and take note of its address.

3. **Complete the Challenge:**
   - Run the provided challenge instance.
   - When prompted, enter the hexadecimal address of the `win` function that you identified in GDB.

4. **Retrieve the Flag:**
   - By providing the correct address of the `win` function, the program will jump to that address.
   - The program will execute the `win` function, which will print the flag.

## Flag
Congratulations! You have successfully solved the "Picker IV" reverse engineering challenge. By identifying the address of the `win` function within the binary and providing it to the challenge instance, you've obtained the flag.
