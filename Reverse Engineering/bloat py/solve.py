from pwn import * 

with open("flag.txt.enc", "rb") as file: 
  content = file.read()

  print(xor(content, b"rapscallion").decode())