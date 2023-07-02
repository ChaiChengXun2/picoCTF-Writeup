# Information

## Basic Information
Category: Forensics  
Points: 10  

## Solving
The idea of this challenge is to familiarise yourself with Forensics. This challenge contains two processes or steps to get the flag.
  
**Step 1:**  
First download the file  
```
wget https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg
```  

**Step 2:**   
Run exiftool on the image  
```exiftool cat.jpg```  

**Step 3:**   
I found that ```cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9``` resembles base64 and took it to decode. You can use online tools such as [CyberChef](https://cyberchef.org/) or [dcode](https://www.dcode.fr/en)  

Alternatively, you can use a python script  
```
#!/usr/bin/python3

import base64

def main():
	encodedFlag = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
	print(base64.b64decode(encodedFlag))

main()
```

**Step 4:**  
Copy the flag and complete the challenge  
```picoCTF{the_m3tadata_1s_modified}```

**SOLVED**  
