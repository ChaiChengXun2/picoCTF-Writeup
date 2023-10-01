# PW Crack 3 - General Skills Challenge

## Basic Information
- **Name:** PW Crack 3
- **Category:** General Skills
- **Points:** 100

## Objective
The "PW Crack 3" challenge aims to teach participants how to use Python to crack a password-protected flag. Participants are provided with seven possible passwords to crack the encryption.

## Solution
To successfully complete the "PW Crack 3" challenge, you have two methods at your disposal:

### Brute Force Method
1. **Brute Force Each Password:**
   - Given that you have only seven possible passwords, you can manually attempt each one to decrypt the flag.
   - Try each password one by one until you find the correct one.

### Script Method
1. **Script**
    - Given all the necessary files for the encoding, we can decode it as well.
    - The modified code literally just loops through all possible password and tries them  
  
   ```python
   import hashlib
    
    ### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
    def str_xor(secret, key):
        #extend key to secret length
        new_key = key
        i = 0
        while len(new_key) < len(secret):
            new_key = new_key + key[i]
            i = (i + 1) % len(key)        
        return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
    ###############################################################################
    
    flag_enc = open('level3.flag.txt.enc', 'rb').read()
    correct_pw_hash = open('level3.hash.bin', 'rb').read()
    
    def hash_pw(pw_str):
        pw_bytes = bytearray()
        pw_bytes.extend(pw_str.encode())
        m = hashlib.md5()
        m.update(pw_bytes)
        return m.digest()
    
    def level_3_pw_check():
        pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
    
        for pw in pos_pw_list:
            user_pw_hash = hash_pw(pw)
            if( user_pw_hash == correct_pw_hash ):
                print("Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), pw)
                print(decryption)

    level_3_pw_check()
   ```

## Flag
Congratulations! You have successfully solved the "PW Crack 3" general skills challenge. By either manually attempting each password or reverse engineering and running the provided script, you've obtained the flag:

