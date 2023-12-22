# convertme.py - General Skills Challenge

## Challenge Overview
**Name:** convertme.py  
**Category:** General Skills  
**Points:** 100

## Objective

In the "convertme.py" challenge, the objective is to reverse engineer the provided Python source code, which is used to encrypt the flag. We aim to understand the encryption process, extract the necessary information, and decode the flag.

## Solution Steps

To solve this challenge, we follow these steps:

1. **Review the Source Code:**
   - Begin by examining the Python script, "convertme.py," that's provided in the challenge. This is crucial to understand the encryption process and identify the encryption method.

2. **Understanding XOR Encryption:**
   - This challenge uses XOR (exclusive OR) encryption, which is a simple yet reversible operation. XORing data with the same key twice results in the original data.

3. **Extract the Relevant Code:**
   - To make the decryption process more manageable, extract the key elements of the code that are responsible for the XOR encryption. Copy these sections into a new file for analysis.

4. **Reverse the XOR Operation:**
   - Implement the reverse XOR operation in the new file. XORing the encrypted data with the same key used for encryption will reveal the original flag.

5. **Run the Decryption Script:**
   - Execute the Python script with the decryption logic you implemented. This should yield the decrypted flag.

By understanding the XOR encryption method and implementing the reverse XOR operation, you can successfully decrypt the flag. XOR encryption is reversible, making it possible to uncover the original flag.

```python
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x4c) + chr(0x06) + chr(0x5d) + chr(0x09) + chr(0x5e) + chr(0x00) + chr(0x41) + chr(0x01) + chr(0x13)

flag = str_xor(flag, 'enkidu')

print(flag)
```
**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
