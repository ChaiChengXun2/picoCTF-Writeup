# Safe Opener 2 - CTF Challenge Writeup

Challenge: Safe Opener 2
Points: 100
Category: Reverse Engineering

## Objective
The objective of the Safe Opener 2 challenge is to learn about Java programming and reverse engineering. You will need to decompile a Java class file to discover the hidden flag.

## Solution
To successfully complete this challenge, follow these steps:

1. **Open the Java class file**: Start by opening the provided Java class file in a text editor.

2. **Hex table**: Upon opening the file, you may notice that it contains a hex table. This hex table is because the file is in the .class format, which is a compiled Java class file.

3. **Decompile the .class file**: To access the contents of the Java class file, you need to decompile it. Decompilation will convert the compiled bytecode back into human-readable Java code.

4. **Use a decompiler tool**: In this case, you can use a decompiler tool such as ```jd-gui```. Open the .class file in ```jd-gui```, and it will decompile the contents into a readable format.

5. **Discover the flag**: Within the decompiled code, search for the hidden flag.

6. Use the discovered flag to complete the challenge.

7. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you need to discover.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Enjoy exploring Java decompilation and reverse engineering, and happy hacking!
