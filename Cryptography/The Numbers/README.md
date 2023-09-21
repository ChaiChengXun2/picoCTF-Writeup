# The Numbers

## Basic Information
Category: Cryptography
Points: 50  

## Solving
The concept of this challenge is to familiarise yourself with ASCII.  
  
**Step 1:**  
Download & view the picture. You will find some encoding. By adding 96 to each number, you can get the corresponding ASCII value that yields the flag.     
```python
def main():
	encoded = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"

	encoded = encoded.split(" ")

	flag = ""

	for char in encoded:
		if char in "{}":
			flag += char
		else:
			flag += chr(int(char) + 96)

	print(flag)

main()
```

**Step 3:**   
Copy and paste the flag to complete the challenge  
```picoctf{thenumbersmason}```  

**SOLVED**  
