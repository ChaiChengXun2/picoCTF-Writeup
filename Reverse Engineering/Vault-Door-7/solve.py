ints = ["1096770097", "1952395366", "1600270708", "1601398833", "1716808014", "1734291511", "960049251", "1681089078"]
binaries = []

flag = ""

def divide_string(string, parts):
   part_length = len(string) // parts
   substrings = [string[i:i + part_length] for i in range(0, len(string), part_length)]
   if len(substrings) > parts:
      substrings[-2] += substrings[-1]
      substrings.pop()
   return substrings

for number in ints:
	binary_number = bin(int(number))[2:]

	while len(binary_number) != 32:
		binary_number = "0" + binary_number

	parts = 4
	binaries.extend(divide_string(binary_number, parts))

for binary in binaries:
	flag += chr(int(binary, 2))

print(flag)