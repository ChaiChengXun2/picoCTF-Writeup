def main():
	encoded = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

	flag = ""

	for char in encoded:
		if char in "{}_":
			flag += char
		elif char.islower():
			if ord(char) + 13 >= 97 and ord(char) + 13 <= 122:
				flag += chr(ord(char) + 13)
			else:
				flag += chr(ord(char) + 13 - 26)
		elif char.isupper():
			if ord(char) + 13 >= 65 and ord(char) + 13 <= 90:
				flag += chr(ord(char) + 13)
			else:
				flag += chr(ord(char) + 13 - 26)

	print(flag)
		

main()
