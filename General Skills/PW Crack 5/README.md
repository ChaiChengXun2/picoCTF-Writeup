# PW Crack 5 - General Skills Challenge

## Basic Information
- **Name:** PW Crack 5
- **Category:** General Skills
- **Points:** 100

## Objective
The "PW Crack 5" challenge aims to teach participants how to use Python to crack a password-protected flag. In this challenge, participants are provided with a dictionary of possible passwords.

## Solution
To successfully complete the "PW Crack 5" challenge, you need to modify the provided Python script to iterate through the dictionary of possible passwords and find the correct one. Here's a step-by-step solution:

1. **Examine the Provided Python Script:**
   - Start by examining the provided Python script, named `level5.py`, in detail.

2. **Modify the Script for Dictionary Attack:**
   - Modify the script to open the dictionary file, read its contents, and iterate through each password.

3. **Run the Modified Script:**
   - Execute the modified Python script with the dictionary of possible passwords.
   - The script will iterate through the dictionary and print the decrypted flag when the correct password is found.

4. **Example of a Modified Script:**
   - Below is an example of a modified script for "PW Crack 5":

```python
import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    # Extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])
###############################################################################

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_5_pw_check():
    with open("dictionary.txt", "r") as file:
        dictionary = file.readlines()

        for password in dictionary:
            user_pw_hash = hash_pw(password[:-1])
            if( user_pw_hash == correct_pw_hash ):
                print("Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), password[:-1])
                print(decryption)
                return
                
level_5_pw_check()
