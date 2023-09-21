# Crackme-py - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering  
**Points:** 30  

## Objective

The "Crackme-py" challenge aims to test your reverse engineering skills and your ability to decode text encoded using ROT47 encoding.

## Solution

To successfully complete the "Crackme-py" challenge, follow these steps:

### Step 1: Download and Analyze Python File

1. **Download and View Python File:**
   - Begin by downloading the provided Python file.
   - Open the file in a text editor or code editor to examine its contents.
   - Comments within the file hint that it uses ROT47 encoding.

### Step 2: Decode ROT47 Encoding

2. **Decode Using CyberChef or Python:**
   - To decode the ROT47-encoded text, you have two options:
     - Option 1: Use an online tool like [CyberChef](https://cyberchef.org). Simply paste the encoded text into the tool and select the ROT47 operation to decode it.
     - Option 2: Use a Python program to decode it programmatically. Here's a Python script that accomplishes this:

   ```python
   def main():
       password = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"

       answer = ""

       for letter in password:
           if ord(letter) + 47 < 127:
               answer += chr(ord(letter) + 47)
           else:
               answer += chr(ord(letter) + 47 - 94)

       print(answer)

   main()
   ```
Flag: picoCTF{XXXXXXXXX}  

**Challenge Solved**  
