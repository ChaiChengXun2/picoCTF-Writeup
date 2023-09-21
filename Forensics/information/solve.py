#!/usr/bin/python3

import base64

def main():
	encodedFlag = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
	print(base64.b64decode(encodedFlag))

main()
