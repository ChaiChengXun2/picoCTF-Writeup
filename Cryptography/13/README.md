# 13

## Basic Information
Category: Cryptography  
Points: 100   

## Solving
The concept of this challenge is to familiarise yourself with ROT13.   
  
**Step 1:**  
You can use online tools or write python scripts. CyberChef: [CyberChef](https://cyberchef.org) can crack ROT13 encoded messages.     
```
def main():
	encoded = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

	flag = ""

	for char in encoded:
		if char in "{}_":
			flag += char
		elif char.islower():
			if ord(char) + 13 >= 97 and ord(char) + 13 <= 122:
				flag += chr(ord(char) + 13)
			else:
				flag += chr(ord(char) + 13 - 26)
		elif char.isupper():
			if ord(char) + 13 >= 65 and ord(char) + 13 <= 90:
				flag += chr(ord(char) + 13)
			else:
				flag += chr(ord(char) + 13 - 26)

	print(flag)
		

main()
```

**Step 2:**   
Copy and paste the flag to complete the challenge  
```picoCTF{not_too_bad_of_a_problem}```  

**SOLVED**  
