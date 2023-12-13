# Speeds and Feeds - Reverse Engineering Challenge

## Basic Information
**Name:** Speeds and Feeds  
**Category:** Reverse Engineering  
**Points:** 50

## Objective

The "Speeds and Feeds" challenge dives into the realm of reverse engineering. Your objective is to decipher a G-code program by connecting to a provided instance and utilize the provided resources to uncover the hidden flag.

## Solution

To successfully complete the "Speeds and Feeds" challenge, follow these steps:

1. **Connect to the Provided Instance:**
   - Begin by connecting to the instance provided for this challenge. Upon connection, you'll discover a G-code program.

2. **Copy the G-code Program:**
   - Instead of manually copying and pasting the G-code program, which might be cumbersome, consider using a Python program to automate this process. This will ensure accuracy and save time.
      ```python
      from pwn import * 

      content = ""

      with remote("mercury.picoctf.net",  7032) as connection:
        content = connection.clean(1).decode()


      with open("output.txt", "w") as file: 
        file.write(content)

      ```

3. **Identify the G-code Language:**
   - The challenge hints at a CNC machine and the language it uses. Recognize that the program is written in G-code, which is the language commonly used to control CNC machines.

4. **View the G-code in an Online G-code Viewer:**
   - After obtaining the G-code program, you'll need a way to visualize it. Utilize an online G-code viewer, such as [https://ncviewer.com/](https://ncviewer.com/), to upload the G-code file.

5. **Decode and Analyze the Output:**
   - Once the G-code program is uploaded to the viewer, inspect the generated visual output. Search for any hidden messages or patterns that may contain the flag.

Flag: picoCTF{XXXXXXXXXX}

**Challenge Solved**  
