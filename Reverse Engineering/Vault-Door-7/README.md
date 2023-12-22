# Vault-Door-7 - Reverse Engineering Challenge

## Challenge Overview
**Name:** Vault-Door-7  
**Category:** Reverse Engineering  
**Points:** 400

## Objective

In the "Vault-Door-7" challenge, the objective is to reverse engineer a Java program that encodes a flag in a unique manner. The encoding process involves converting each character of the flag into binary code, grouping these binary codes in sets of four, and then converting them into integers. The challenge requires reversing this process to reveal the flag.

## Solution Steps

To successfully complete this challenge, follow these steps:

1. **Examine the Provided Explanation:**
   - Open the provided Java source code and carefully read the detailed explanation provided in the challenge.

2. **Understand the Encoding Process:**
   - Review and understand the encoding process outlined in the explanation:
     - The flag's characters are first converted into binary code.
     - These binary codes are grouped together in sets of four.
     - The binary code of four characters is then combined into a larger binary representation.
     - Finally, the large binary representation is converted into an integer.

3. **Reverse the Encoding Process:**
   - Begin the reversal process:
     - Take the given integer and convert it back to its binary form.
     - Split the binary representation into four equal parts, as indicated in the explanation.
     - Find the ASCII character associated with each four-character binary group.

4. **Reveal the Flag:**
   - By successfully reversing the encoding process as described above, you'll reveal the flag hidden within the challenge.

By understanding and reversing the encoding process, you can obtain the original flag in the "Vault-Door-7" challenge.

```python
ints = ["1096770097", "1952395366", "1600270708", "1601398833", "1716808014", "1734291511", "960049251", "1681089078"]
binaries = []

flag = ""

def divide_string(string, parts):
   part_length = len(string) // parts
   substrings = [string[i:i + part_length] for i in range(0, len(string), part_length)]
   if len(substrings) > parts:
      substrings[-2] += substrings[-1]
      substrings.pop()
   return substrings

for number in ints:
	binary_number = bin(int(number))[2:]

	while len(binary_number) != 32:
		binary_number = "0" + binary_number

	parts = 4
	binaries.extend(divide_string(binary_number, parts))

for binary in binaries:
	flag += chr(int(binary, 2))

print(flag)
```

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
