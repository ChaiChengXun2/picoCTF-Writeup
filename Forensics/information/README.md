# Information - Forensics Writeup

## Basic Information
**Category:** Forensics  
**Points:** 10  

## Objective

The "Information" challenge is designed to introduce you to the field of digital forensics. This challenge consists of a series of steps to uncover the hidden flag.

## Solution

To successfully complete the "Information" challenge, follow these steps:

### Step 1: Download the Image

1. **Download the Image:**
   - Begin by downloading the provided image using the `wget` command:
     ```
     wget <link>
     ```

### Step 2: Analyze Image Metadata

2. **Run `exiftool` on the Image:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you downloaded the image.
   - Run the following command to examine the image's metadata:
     ```
     exiftool <image>
     ```

### Step 3: Decode Base64 String

3. **Identify Base64 String:**
   - In the output from `exiftool`, you may notice a string that resembles Base64:
     ```
     cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
     ```

4. **Decode Base64:**
   - To reveal the flag, decode the Base64 string.
   - You can use online tools like [CyberChef](https://cyberchef.org/) or [dcode](https://www.dcode.fr/en) for this purpose.

Alternatively, you can use a Python script to decode the Base64 string.

### Step 4: Use Python Script (Optional)

5. **Use a Python Script (Optional):**
   - If you prefer a Python solution, here's a script that decodes the Base64 string:
   
   ```python
   #!/usr/bin/python3

   import base64

   def main():
       encodedFlag = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
       print(base64.b64decode(encodedFlag))

   main()
   ```  
Flag: picoCTF{XXXXXXXXXX}

**Challenge Solved**  
