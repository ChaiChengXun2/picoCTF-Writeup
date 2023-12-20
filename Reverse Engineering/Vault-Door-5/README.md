# Vault-Door-5 - Reverse Engineering Challenge

## Challenge Overview
**Name:** Vault-Door-5  
**Category:** Reverse Engineering  
**Points:** 300

## Objective

In the "Vault-Door-5" challenge, the objective is to reverse engineer a Java program to reveal a hidden flag. The program uses base64 encoding, but the flag is further encoded in URL encoding.

## Solution Steps

To successfully complete this challenge, follow these steps:

1. **Inspect the Java Source Code:**
   - Open the provided Java source code file, which is the starting point for this reverse engineering challenge.

2. **Identify Base64 Encoding:**
   - Examine the Java code to identify the usage of base64 encoding.
   - In the code, you'll find a base64-encoded message.

3. **Decode Base64:**
   - Using a base64 decoder, decode the base64-encoded message to reveal its content.

4. **Recognize URL Encoding:**
   - After decoding the base64 message, you may find that it is URL encoded.
   - URL encoding replaces certain characters with "%XX" where "XX" is the hexadecimal value of the character.

5. **Decode URL Encoding:**
   - Apply URL decoding to the previously decoded content. This will convert the URL-encoded characters back to their original form.

6. **Uncover the Flag:**
   - The result of the URL decoding will provide you with the unscrambled flag, which is the solution to the challenge.

By identifying the base64 encoding, decoding it, and then dealing with the URL encoding, you'll successfully uncover the hidden flag in the "Vault-Door-5" challenge.

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
