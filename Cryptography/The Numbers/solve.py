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
