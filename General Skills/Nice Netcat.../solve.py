#!/usr/bin/python3

def main():
	flag = []
	encodedFlag = "112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 55 99 48 56 50 49 102 53 125 10".split(" ")
	for char in encodedFlag:
		flag.append(chr(int(char)))
	print(''.join(flag))

main()
