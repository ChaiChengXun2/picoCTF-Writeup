# Transformation

## Basic Information
Category: Reverse Engineering   
Points: 20  

## Solving
I have no idea what the concept of the challenge is
  
**Step 1:**  
Python script to solve the challenge  
```
import codecs

def main():
	with open("enc") as file: 
		lines = file.readlines()

		answer = ""

		for char in lines[0]:
			answer += hex(ord(char))[2:]

	flag = codecs.decode(answer, "hex").decode("ASCII")  
	print(flag)

main()
```

**Step 2:**   
Copy and paste the flag to complete the challenge  
```picoCTF{16_bits_inst34d_of_8_04c0760d}```  

**SOLVED**  
