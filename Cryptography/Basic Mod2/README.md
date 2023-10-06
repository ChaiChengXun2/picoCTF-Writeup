# Basic Mod2 - CTF Challenge Writeup

Challenge: Basic Mod2
Points: 100
Category: Cryptography

## Objective
The objective of the Basic Mod2 challenge is to learn about cryptography, specifically modular arithmetic (mod) and modular inverse. You will need to decrypt a given message that has been encrypted using these techniques.

## Solution
To successfully complete this challenge, follow these steps:

1. **Online tool limitations**: Using online tools may not be effective for solving this challenge, as you are required to take the modular inverse and map the numbers onto a custom character set.

2. **Python script solution**: To decrypt the message, you can write a Python script. The character set used in the decryption is "-ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_".

Here's a sample Python script to decrypt the message:

```python
character_set = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
encrypted_flag = "432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63"

# Split the encrypted flag into individual numbers
encrypted_flag = encrypted_flag.split(" ")

flag = ""

# Decrypt each number using modular inverse and map it to the character set
for item in encrypted_flag:
    index = pow(int(item), -1, 41)
    flag += character_set[index]

print(flag)
```