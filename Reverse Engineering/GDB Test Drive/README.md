# GDB Test Drive - Reverse Engineering Challenge

## Basic Information
- **Name:** GDB Test Drive
- **Category:** Reverse Engineering
- **Points:** 100

## Objective
The "GDB Test Drive" challenge is designed to introduce participants to GDB (GNU Debugger) and its capabilities in reverse engineering tasks.

## Solution
To successfully solve the "GDB Test Drive" challenge, follow these steps:

1. **Execute GDB:**
   - Begin by running GDB on the provided executable file.
   - Open your terminal and enter the following command, replacing `<filename>` with the name of the executable:
     ```
     gdb <filename>
     ```

2. **Set a Breakpoint:**
   - Set a breakpoint just before the `sleep` function in the program. You want to stop the program's execution right before it enters the sleep period.
     ```
     break *(main+99)
     ```

3. **Run the Program:**
   - Start the program within GDB by typing:
     ```
     run
     ```

4. **Skip the Sleep Function:**
   - Once the program reaches the breakpoint at the `sleep` function, you can jump out of the sleep function to skip the sleep duration.
     ```
     jump *(main+104)
     ```

5. **Program Resumes Execution:**
   - After jumping out of the sleep function, the program will continue its execution as if the sleep function never occurred.

6. **Capture the Flag:**
   - As a result of skipping the sleep function, the program will reveal the flag and complete the intended operation.

7. **Challenge Completed:**
   - Congratulations! You have successfully completed the "GDB Test Drive" challenge by using GDB to skip the sleep function and allow the program to continue its execution.

## Flag
Great job! You've completed the "GDB Test Drive" reverse engineering challenge and obtained the flag
