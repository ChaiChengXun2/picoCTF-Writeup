# Crackme-py

## Basic Information
Category: Reverse Engineering  
Points: 30  

## Solving
The concept of this challenge is to familiarise yourself with python and ROT47 encoding. 
  
**Step 1:**  
Download and view the python file. Comments in the file indicate that it is using ROT47 encoding. There are many tools that could solve ROT47. CyberChef: [CyberChef](https://cyberchef.org) is one of them. Or alternatively you can use python program to solve it. 

```
def main():
	password = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"

	answer = ""

	for letter in password:
		if ord(letter) + 47 < 127:
			answer += chr(ord(letter) + 47)
		else:
			answer += chr(ord(letter) + 47 - 94)

	print(answer)

main()
```

**Step 3:**   
Copy and paste the flag to complete the challenge  
```picoCTF{1|\/|_4_p34|\|ut_dd2c4616}```  

**SOLVED**  
