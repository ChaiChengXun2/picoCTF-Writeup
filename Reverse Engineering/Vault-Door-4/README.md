# Vault-Door-4 - Reverse Engineering Challenge

## Challenge Overview
**Name:** Vault-Door-4  
**Category:** Reverse Engineering  
**Points:** 250

## Objective

In the "Vault-Door-4" challenge, the objective is to decode numbers provided in different formats (hexadecimal, octal, and decimal) and convert them to ASCII characters. The numbers are extracted from a Java source code file, and the decoded data contains the flag.

## Solution Steps

To successfully complete this challenge, follow these steps:

1. **Examine the Java Source Code:**
   - Open the provided Java source code, which is the starting point for this reverse engineering challenge.

2. **Identify Numeric Values:**
   - Carefully inspect the code and locate the numeric values used as part of the challenge.
   - You'll notice numbers with various prefixes, which indicate their respective formats:
     - Numbers prefixed with "0x" are in hexadecimal format.
     - Numbers without any prefix are in decimal format.
     - Numbers prefixed with "0" are in octal format.

3. **Convert Numbers to ASCII:**
   - Collect all the numeric values and their respective formats.
   - Convert each of these numbers into ASCII characters using the correct format conversion.
   - For example, hexadecimal numbers should be converted to ASCII, octal numbers to ASCII, and decimal numbers to ASCII.

4. **Uncover the Flag:**
   - As you decode each number, the result is a series of ASCII characters.
   - When you've successfully converted all the numbers, you will have revealed the complete, unscrambled flag.

By recognizing the various numeric formats and decoding them to their respective ASCII characters, you'll ultimately expose the hidden flag.

```python
decimals = "106 85 53 116 95 52 95 98"
decimals = decimals.split(" ")

hexadecimals = "0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f"
hexadecimals = hexadecimals.split(", ")

octals = "0142, 0131, 0164, 063, 0163, 0137, 0143, 061"
octals = octals.split(", ")

normal = '9' + '4' + 'f' + '7' + '4' + '5' + '8' + 'e'

flag = ""

for dec in decimals:
	flag += chr(int(dec))

for hexadecimal in hexadecimals:
	flag += bytearray.fromhex(hexadecimal[2:]).decode()

for octal in octals:
	flag += chr(int(octal[1:], 8))

print(flag+normal)
```

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
