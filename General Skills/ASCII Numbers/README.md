# ASCII Numbers - General Skills Writeup

## Basic Information
**Category:** General Skills  
**Points:** 100

## Objective

The "ASCII Numbers" challenge aims to acquaint you with hexadecimal encoding and decoding. The objective is to decode a given hexadecimal-encoded string to reveal the hidden flag.

## Solution

To successfully complete the "ASCII Numbers" challenge, you have two methods at your disposal:

### Method 1: Using CyberChef

1. **Utilize Online Tools:**
   - As hinted in the challenge description, you can conveniently decode the hexadecimal-encoded string using online tools like [CyberChef](https://gchq.github.io/CyberChef/).

2. **Access CyberChef Hex Tool:**
   - Visit the CyberChef website.
   - In the top-left corner, locate the "Operations" dropdown menu and select "Hex."

3. **Input the Encrypted Flag:**
   - Paste the provided hexadecimal-encoded string into the input field.

4. **Decode the Flag:**
   - CyberChef will automatically decode the hexadecimal string and display the flag.

### Method 2: Using a Python Script

1. **Use a Python Script:**
   - Alternatively, you can use a Python script to decode the flag. Below is a Python script that decodes the provided hexadecimal-encoded string:
   
   ```python
   encrypted_flag = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x35 0x63 0x31 0x31 0x5f 0x6e 0x30 0x5f 0x71 0x75 0x33 0x35 0x37 0x31 0x30 0x6e 0x35 0x5f 0x31 0x6c 0x6c 0x5f 0x74 0x33 0x31 0x31 0x5f 0x79 0x33 0x5f 0x6e 0x30 0x5f 0x6c 0x31 0x33 0x35 0x5f 0x34 0x34 0x35 0x64 0x34 0x31 0x38 0x30 0x7d"
   
   hexadecimals = encrypted_flag.split(" ")
   
   flag = ""
   
   for hexadecimal in hexadecimals: 
       flag += bytearray.fromhex(hexadecimal[2:]).decode()
   
   print(flag)
    ```  
2. **Execute the Python Script**:
   - Run the Python script, and it will decode the hexadecimal-encoded string, revealing the flag.  

With either of these methods, you will successfully decode the flag and complete the "ASCII Numbers" challenge.  

flag: picoCTF{XXXXXXX}  

**Challenge Solved**  
