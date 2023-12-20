# Bit-O-Asm-4

## Basic Information
Category: Reverse Engineering  
Difficulty: Easy  
Points: 100  

## Solving
The objective of this challenge is to continue practicing your knowledge of assembly language, with a focus on understanding more complex operations involving conditional jumps.

**Step 1:**  
Examine the provided file, which contains assembly code. Unlike previous Bit-O-Asm challenges, this one involves more operations and introduces conditional jumps, specifically "jle" (jump less than or equal) and "cmp" (compare).

**Step 2:**   
To understand the operations performed on EAX, follow these steps:
- The code compares the value at register rbp-0x4 with 0x2710 using:
    - ```cmp DWORD PTR [rbp-0x4],0x2710```
- If rbp-0x4 is less than or equal to 0x2710, it will execute a jump.
    - ```jle    0x55555555514e <main+37>``` 
- Since rbp-0x4 is not less than 0x2710, the jump is not taken.
- The code proceeds to subtract 0x65 from rbp-0x4 using:
    - ```sub DWORD PTR [rbp-0x4],0x65```

**Step 3:**   
Essentially, the flag will be: original value of ```DWORD PTR [rbp-0x4] - 0x65```
