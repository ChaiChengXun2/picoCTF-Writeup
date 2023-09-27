# GDB Baby Step 1 - Reverse Engineering Challenge

## Basic Information
- **Name:** GDB Baby Step 1
- **Category:** Reverse Engineering
- **Points:** 100

## Objective
The "GDB Baby Step 1" challenge aims to introduce participants to GDB (GNU Debugger) and provides an opportunity to practice basic debugging techniques.

## Solution
To successfully solve the "GDB Baby Step 1" challenge, follow these steps:

1. **Download the File:**
   - Begin by downloading the provided file, which contains the executable that you need to analyze.

2. **Run GDB:**
   - Open your terminal and run GDB on the downloaded file. Replace `<filename>` with the name of the downloaded executable:
     ```
     gdb <filename>
     ```

3. **Set Disassembly Flavor:**
   - Set the disassembly flavor to "intel" to make the disassembly output more readable. Enter the following command within GDB:
     ```
     set disassembly-flavor intel
     ```

4. **Disassemble the Main Function:**
   - Disassemble the `main` function to inspect the assembly code. This will allow you to analyze the program's logic.
     ```
     disassemble main
     ```

5. **Inspect the EAX Register:**
   - Examine the assembly code within the `main` function and look for any operations that affect the EAX register.

6. **Convert Hex to Decimal:**
   - Find the value in the EAX register and convert it to decimal as instructed in the CTF challenge.

7. **Capture the Flag:**
   - Once you've successfully converted the hex value to decimal, you will have the flag.

8. **Challenge Completed:**
   - Congratulations! You've completed the "GDB Baby Step 1" reverse engineering challenge by using GDB to analyze the executable, identify the relevant value in the EAX register, and obtain the flag.

## Flag
Well done! You've successfully solved the "GDB Baby Step 1" reverse engineering challenge and acquired the flag
