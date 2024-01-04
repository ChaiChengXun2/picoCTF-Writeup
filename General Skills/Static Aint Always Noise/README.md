# Static ain't always noise - General Skills Challenge

## Challenge Overview
**Name:** Static ain't always noise  
**Category:** General Skills  
**Points:** 20

## Objective

The objective of the "Static ain't always noise" challenge is to obtain the flag by analyzing a given bash script and ELF binary to extract the flag hidden within the binary.

## Solution Steps

To solve this challenge, follow these steps:

1. **Obtain Challenge Files:**
   - Begin by downloading the provided challenge files, which include a bash script and an ELF binary.

2. **Analyze the Bash Script:**
   - Start by examining the bash script.
   - The bash script appears to be a tool for disassembling the ELF binary, potentially revealing useful information.

3. **Make the Script Executable:**
   - To use the bash script, make it executable using the `chmod` command:
     ```
     chmod +x <script>
     ```

4. **Run the Script:**
   - Execute the script with the ELF binary as an argument:
     ```
     sh <bash script> <binary>
     ```

5. **Analyze the Output:**
   - The script should process the binary and potentially display its disassembled content.
   - While analyzing the output, look for any hints or hidden flag information.

6. **Search for the Flag:**
   - Search through the output, potentially using tools like `grep`, to locate the flag.
   - The flag is typically in the format `picoCTF{XXXXXXXXXX}`.

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
