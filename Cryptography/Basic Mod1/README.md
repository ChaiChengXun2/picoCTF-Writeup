# Basic Mod1 - CTF Challenge Writeup

Challenge: Basic Mod1
Points: 100
Category: Cryptography

## Objective
The objective of the Basic Mod1 challenge is to learn about cryptography, specifically modular arithmetic (mod). You will be required to decrypt a given message encrypted using the modulo operation.

## Solution
To successfully complete this challenge, follow these steps:

1. **Understand the encryption method**: The challenge informs you that the encryption method used is modulo 37 (mod37).

2. **Use of online tools**: Online tools may not be effective for solving this challenge because you are required to apply the modulo operation to each number and map it onto a custom character set.

3. **Python script solution**: To decrypt the message, you can write a Python script. The character set used in the decryption is "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_". 

Here's a sample Python script to decrypt the message:

```python
character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
encrypted_flag = "128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"

# Split the encrypted flag into individual numbers
encrypted_flag = encrypted_flag.split(" ")

flag = ""

# Decrypt each number using mod 37 and map it to the character set
for item in encrypted_flag:
    flag += character_set[int(item) % 37]

print(flag)
```

**Solved**