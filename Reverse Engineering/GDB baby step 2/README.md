# GDB Baby Step 2 - Reverse Engineering Challenge

## Basic Information
- **Name:** GDB Baby Step 2
- **Category:** Reverse Engineering
- **Points:** 100

## Objective
The "GDB Baby Step 2" challenge aims to help participants understand and utilize GDB (GNU Debugger) for reverse engineering tasks.

## Solution
To successfully complete the "GDB Baby Step 2" challenge, follow these steps:

1. **Run GDB:**
   - Start by running GDB on the provided file, similar to previous challenges:
     ```
     gdb <filename>
     ```

2. **Set Disassembly Flavor:**
   - For better code readability, set the disassembly flavor to "intel" within GDB:
     ```
     set disassembly-flavor intel
     ```

3. **Disassemble the Main Function:**
   - Disassemble the `main` function to view the assembly code and understand the program's logic:
     ```
     disassemble main
     ```

4. **Quick Solution (Optional):**
   - If you prefer to quickly solve the challenge without diving deep into the code:
     - Set a breakpoint just before the `main` function returns:
       ```
       break *main+59
       ```
     - Start the program execution:
       ```
       run
       ```
   - This step allows you to extract the necessary information without analyzing the code intricately.

5. **View EAX Value:**
   - After breaking, view the value of the EAX register, which initially holds 123098 (0x1e0da):
     ```
     x $eax
     ```

## In-Depth Analysis
The program exhibits the following characteristics in-depth:

- The program operates as a loop.
- The EAX register begins with the value 123098 (0x1e0da).
- The loop runs for a specific number of iterations 607 (25f).
- During each iteration, the loop counter is added to the EAX register.

Here's a Python representation of the code's logic:

```python
eax = 123098  # or 0x1e0da
loop = 607    # or 25f

for i in range(loop):
    eax += i

print(eax)
