# ASCII FTW - CTF Challenge Writeup

Challenge: ASCII FTW
Points: 100
Category: Reverse Engineering

## Objective
The objective of the ASCII FTW challenge is to reverse engineer a 64-bit ELF executable to reveal the hidden flag. Your task is to analyze the binary, understand its inner workings, and extract the flag.

## Solution
To successfully complete the ASCII FTW challenge, follow these steps:

1. **File Analysis**:
   - Begin by receiving and inspecting the provided file. Run the `file` command to identify the file type, revealing that it's a 64-bit ELF executable.

2. **GDB for Reverse Engineering**:
   - Reverse engineering is the key to solving this challenge. Utilize the GNU Debugger (GDB) to disassemble and analyze the binary.
   - Run GDB with the binary:
     ```
     gdb asciiftw
     ```

3. **GDB Configuration**:
   - Configure GDB for better visibility and control during the analysis:
     - Disable pagination to prevent breaks when viewing long output:
       ```
       set pagination off
       ```
     - Set the disassembly flavor to Intel syntax for clarity:
       ```
       set disassembly-flavor intel
       ```

4. **Disassemble Main Function**:
   - Disassemble the `main` function to examine the binary's logic and operations:
     ```
     disassemble main
     ```

5. **Set a Breakpoint**:
   - To intercept the program's execution after all calculations, set a breakpoint at the appropriate location.

6. **View the Stack**:
   - After hitting the breakpoint, inspect the stack to identify the flag's presence or its generation within the binary.

7. By following these steps and carefully analyzing the binary, you will successfully uncover the hidden flag.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

In the ASCII FTW challenge, your skills in reverse engineering and using GDB are put to the test to extract the flag hidden within the 64-bit ELF executable. Good luck!
