# Nice Netcat...

## Basic Information
Category: General Skills   
Points: 15  

## Solving
The concept of this challenge is to familiarise yourself with netcat.
  
**Step 1:**  
Connect to the server given and you will be given a bunch of ASCII values.    
```
nc mercury.picoctf.net 43239
```

**Step 4:**   
Convert the ASCII to text using online tools or a python script  
```
#!/usr/bin/python3

def main():
	flag = []
	encodedFlag = "112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 55 99 48 56 50 49 102 53 125 10".split(" ")
	for char in encodedFlag:
		flag.append(chr(int(char)))
	print(''.join(flag))

main()
```  

**Step 3:**   
Copy and paste the flag to complete the challenge  
```picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}```  

**SOLVED**  
