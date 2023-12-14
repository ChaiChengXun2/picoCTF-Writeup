# Bit-O-Asm-3

## Basic Information
Category: Reverse Engineering  
Difficulty: Easy  
Points: 100  

## Solving
The objective of this challenge is to continue practicing your knowledge of assembly language, with a focus on understanding more complex operations.

**Step 1:**  
Examine the provided file, which contains assembly code. Unlike Bit-O-Asm-1 and Bit-O-Asm-2, this challenge involves more operations, including multiplication (imul) and addition (add).

**Step 2:**   
To understand the operations performed on EAX, follow these steps:
- Start with the original value of EAX: 0x9fe1a 
    -  ```mov DWORD PTR [rbp-0xc],0x9fe1a```
- Multiply EAX by 4 using DWORD PTR [rbp-0x8]: 0x4
    - ```imul eax, DWORD PTR [rbp-0x8]```
- Add 0x1f5 to the result 
    - ```add eax, 0x1f5```

**Step 3:**   
Calculate the final value of EAX after these operations.

**Step 4:**   
Convert the final value of EAX from hexadecimal to decimal.
