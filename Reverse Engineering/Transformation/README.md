# Transformation - Reverse Engineering Writeup

## Basic Information
**Category:** Reverse Engineering   
**Points:** 20  

## Objective

The "Transformation" challenge involves deciphering the given information to find the flag. The exact concept of the challenge may not be evident initially.

## Solution

To successfully complete the "Transformation" challenge, follow these steps:

### Step 1: Python Script to Decode

1. **Use Python Script:**
   - A Python script can be used to decode the contents of a file named "enc." The script performs the necessary transformations to reveal the flag.

   ```python
   import codecs

   def main():
       with open("enc") as file: 
           lines = file.readlines()

           answer = ""

           for char in lines[0]:
               answer += hex(ord(char))[2:]

       flag = codecs.decode(answer, "hex").decode("ASCII")  
       print(flag)

   main()
   ```  

flag: picoCTF{XXXXXXXXXX}  

**Challenge Solved**  
