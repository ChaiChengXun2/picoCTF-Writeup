# PW Crack 4 - General Skills Challenge

## Basic Information
- **Name:** PW Crack 4
- **Category:** General Skills
- **Points:** 100

## Objective
The "PW Crack 4" challenge aims to teach participants how to use Python to crack a password-protected flag. In this challenge, participants are presented with 100 possible passwords to decrypt the flag.

## Solution
To successfully complete the "PW Crack 4" challenge, you have two methods at your disposal:

### Brute Force Method
1. **Brute Force All Possible Passwords:**
   - Given that you have a list of 100 possible passwords, attempting each one manually is impractical.
   - Instead, you can modify the provided Python script to perform the brute force attack on your behalf.

2. **Modify the Provided Python Script:**
   - Examine the provided Python script, named `level4.py`, in detail.
   - The script contains a list of possible passwords and the correct password hash, as well as a function named `str_xor` and a password hashing function.
   - Modify the script to iterate through the list of possible passwords and attempt each one by hashing it and comparing it to the correct password hash.
   - When a match is found, the script will decrypt the flag and print it.

3. **Run the Modified Script:**
   - Execute the modified Python script with the provided passwords and correct password hash.
   - The script will perform the brute force attack and print the decrypted flag when the correct password is found.

### Modified Script Example
Below is an example of a modified script:

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

flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_4_pw_check():
    pos_pw_list = [  # Add your list of 100 possible passwords here ]
    for password in pos_pw_list:
        user_pw_hash = hash_pw(password)
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), password)
            print(decryption)
            return

level_4_pw_check()
