# Vault-Door-3 - Reverse Engineering Challenge

## Challenge Overview
**Name:** Vault-Door-3  
**Category:** Reverse Engineering  
**Points:** 200

## Objective

In the "Vault-Door-3" challenge, the goal is to reverse engineer a Java program to reveal the hidden flag. The challenge provides us with a Java source code snippet, and our task is to decipher the flag, which is intentionally scrambled within the code.

## Solution Steps

To solve this challenge, we can follow these steps:

1. **Examine the Java Source Code:**
   - Open the provided Java source code snippet, which is the basis for this reverse engineering challenge.

2. **Locate the Scrambled Flag:**
   - Upon examining the code, you'll notice that the flag is present within it.
   - However, the flag is not immediately readable as it's been scrambled within the code.

3. **Understand the Flag Scrambling:**
   - Analyze the code and identify the parts that manipulate and scramble the flag text.
   - Pay close attention to any loops or transformations applied to the flag within the code.

4. **Reverse the Scrambling:**
   - Your task is to reverse the operations applied to the flag text within the code.
   - This might involve identifying the loops that modify the characters of the flag and reversing those transformations.
   - As you reverse these operations, you will gradually reveal the unscrambled flag.

5. **Flag Extraction:**
   - Once you have successfully reversed the flag scrambling, you will uncover the unscrambled flag within the code.
   - The flag should be displayed in a clear and readable format.

By understanding the Java code and meticulously reversing the flag-scrambling process, you can unveil the hidden flag.

```python
scrambled_password = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
password = [None] * 32

i = 0

while i < 8:
	password[i] = scrambled_password[i]
	i += 1

while i < 16:
	password[i] = scrambled_password[23 - i]
	i += 1

while i < 32:
	password[i] = scrambled_password[46 - i]
	i += 2

i = 31
while i >= 17: 
	password[i] = scrambled_password[i]
	i -= 2

print(f"{''.join(password)}")
```

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
