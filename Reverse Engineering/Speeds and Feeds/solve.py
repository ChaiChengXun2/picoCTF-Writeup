from pwn import * 

content = ""

with remote("mercury.picoctf.net",  7032) as connection:
	content = connection.clean(1).decode()


with open("output.txt", "w") as file: 
	file.write(content)
