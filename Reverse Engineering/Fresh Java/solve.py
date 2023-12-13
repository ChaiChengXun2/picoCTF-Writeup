flag = ""

with open("text.txt", "r") as file:
  content = file.readlines() 

  for line in content:
    line = line[:-1].strip()
    flag += line[-3]

print(flag[::-1])