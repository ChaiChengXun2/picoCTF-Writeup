# Mod 26

## Basic Information
Category: Cryptography   
Points: 10  

## Solving
The concept of of this challenge is to familiarise yourself with ROT13.
  
**Step 1:**  
You can use online tools such as [CyberChef](https://cyberchef.org/) or [dcode](https://www.dcode.fr/en)   

Or you can use a python script 
```
#!/usr/bin/python3

import codecs

def main():
	encoded = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"
	print(codecs.decode(encoded, 'rot-13'))

main()
```

**Step 2:**   
Copy and paste the flag to complete the challenge  
```picoCTF{next_time_I'll_try_2_rounds_of_rot13_ZNMldSDw}```  

**SOLVED**  
