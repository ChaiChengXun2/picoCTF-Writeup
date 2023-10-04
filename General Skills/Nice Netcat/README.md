# Nice Netcat... - General Skills Writeup

## Basic Information
**Category:** General Skills   
**Points:** 15  

## Objective

The "Nice Netcat..." challenge is designed to acquaint you with the use of Netcat (`nc`) to communicate with a remote server and decode ASCII values to reveal the flag.

## Solution

To successfully complete the "Nice Netcat..." challenge, follow these steps:

### Step 1: Connect to the Server

1. **Connect to the Server:**
   - Use the `nc` (Netcat) command to connect to the provided server and port:
     ```bash
     nc mercury.picoctf.net 43239
     ```

   - Connecting to the server will provide you with a series of ASCII values.

### Step 2: Convert ASCII to Text

2. **Decode ASCII Values:**
   - You need to decode the received ASCII values to reveal the flag.
   - Here's a Python script that decodes the ASCII values into text:

     ```python
     #!/usr/bin/python3

     def main():
         flag = []
         encodedFlag = "112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 55 99 48 56 50 49 102 53 125 10".split(" ")
         for char in encodedFlag:
             flag.append(chr(int(char)))
         print(''.join(flag))

     main()
     ```

### Step 3: Retrieve and Submit the Flag

3. **Copy and Paste the Flag:**
   - After running the Python script or using alternative methods, you will obtain the flag in plaintext.

4. **Complete the Challenge:**
   - Copy the flag and paste it into the provided submission box on the CTF platform.
   
Flag: `picoCTF{XXXXXXXXXX}`

With these steps, you will successfully connect to the server, decode the ASCII values, and complete the "Nice Netcat..." challenge.

**Challenge Accomplished**
