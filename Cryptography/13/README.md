# 13 - Cryptography Writeup

## Basic Information
**Category:** Cryptography  
**Points:** 100

## Objective

The "13" challenge aims to familiarize you with ROT13, a simple letter substitution cipher that shifts the letters of the alphabet by 13 positions.

## Solution

To successfully complete the "13" challenge, you have two methods at your disposal:

### Method 1: Using CyberChef

1. **Leverage Online Tools:**
   - As hinted in the challenge description, you can conveniently decrypt ROT13-encoded messages using online tools like [CyberChef](https://cyberchef.org).

2. **Access CyberChef ROT13 Tool:**
   - Visit the CyberChef website.
   - In the top-left corner, locate the "Operations" dropdown menu and select "ROT13."

3. **Input the Encrypted Flag:**
   - Paste the provided ROT13-encoded string into the input field.

4. **Decrypt the Flag:**
   - CyberChef will automatically decrypt the ROT13-encoded string and display the flag.

### Method 2: Using a Python Script

1. **Use a Python Script:**
   - Alternatively, you can use a Python script to decrypt the ROT13-encoded message. Below is a Python script that decrypts the provided ROT13-encoded string:
   
   ```python
   def main():
       encoded = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
   
       flag = ""
   
       for char in encoded:
           if char in "{}_":
               flag += char
           elif char.islower():
               if ord(char) + 13 >= 97 and ord(char) + 13 <= 122:
                   flag += chr(ord(char) + 13)
               else:
                   flag += chr(ord(char) + 13 - 26)
           elif char.isupper():
               if ord(char) + 13 >= 65 and ord(char) + 13 <= 90:
                   flag += chr(ord(char) + 13)
               else:
                   flag += chr(ord(char) + 13 - 26)
   
       print(flag)
   
   main()
   ```
2. **Execute the Python Script:**
   - Run the Python script, and it will decrypt the ROT13-encoded string, revealing the flag.  

Flag: picoCTF{XXXXXXXXXX}

**Challenge Solved**  
