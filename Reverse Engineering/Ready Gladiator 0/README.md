# Ready Gladiator 0 - CTF Writeup

- **Name:** Ready Gladiator 0
- **Points:** 100
- **Category:** Reverse Engineering

## Objective

The objective of the "Ready Gladiator 0" challenge is to reverse engineer a Redcode program to find the flag. The provided Redcode program, which is used in the context of Core Wars, contains an error that prevents it from revealing the flag. Your task is to identify and fix the issue to obtain the flag.

## Solution

The solution for this challenge involves understanding the Redcode program and fixing the error that prevents the flag from being revealed.

1. Initial Code:
   - The provided Redcode program is as follows:
     ```redcode
     ;redcode
     ;name Imp Ex
     ;assert 1
     mov 0, 1
     end
     ```
   - The `mov 0, 1` instruction attempts to move a value from address 0 to address 1.

2. Identifying the Issue:
   - The issue in the code is the incorrect order in the `mov` instruction. It should be `mov 1, 0` instead of `mov 0, 1`. This error prevents the program from functioning as intended.

3. Fixing the Error:
   - Change the instruction from:
     ```redcode
     mov 0, 1
     ```
     to:
     ```redcode
     mov 1, 0
     ```

4. Running the Program:
   - After making the correction, you can run the fixed program, and it will reveal the flag.

5. Flag:
   - Once you run the corrected program, you will obtain the flag, which will be in the format `picoCTF{XXXXXXXXXX}`.

