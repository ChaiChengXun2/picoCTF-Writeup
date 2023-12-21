# Vault-Door-6 - Reverse Engineering Challenge

## Challenge Overview
**Name:** Vault-Door-6  
**Category:** Reverse Engineering  
**Points:** 350

## Objective

In the "Vault-Door-6" challenge, the objective is to reverse engineer a Java program to reveal a hidden flag. The program uses hexadecimal characters that are XOR-encoded with 0x55.

## Solution Steps

To successfully complete this challenge, follow these steps:

1. **Examine the Java Code:**
   - Open the provided Java source code file to begin the reverse engineering challenge.

2. **Identify Hexadecimal Encoding:**
   - Inspect the Java code and identify the presence of hexadecimal characters, indicated by the "0x" prefix.
   - Notice that these hexadecimal characters are XOR-encoded with 0x55.

3. **XOR Decoding:**
   - To decode these hexadecimal characters, apply the XOR operation with the key 0x55 (85 in decimal) to each character.
   - XOR operation is reversible, and in this case, it can be used to reverse the encoding.

4. **Reveal the Flag:**
   - Decode all the hexadecimal characters using the XOR decoding method.
   - By performing this decoding process, you will uncover the hidden flag.

By decoding the hexadecimal characters using the XOR operation with the key 0x55, you'll successfully reveal the flag in the "Vault-Door-6" challenge.

```python
hexadecimals = "0x3b 0x65 0x21 0xa 0x38 0x0 0x36 0x1d 0xa 0x3d 0x61 0x27 0x11 0x66 0x27 0xa 0x21 0x1d 0x61 0x3b 0xa 0x2d 0x65 0x27 0xa 0x6c 0x60 0x37 0x30 0x60 0x31 0x36"
hexadecimals = hexadecimals.split(" ")

flag = ""

for hexadecimal in hexadecimals:
	hexadecimal = hexadecimal[2:]
	decimal = int(hexadecimal, 16)

	XOR = decimal ^ 85

	flag += chr(XOR)

print(flag)
```

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
