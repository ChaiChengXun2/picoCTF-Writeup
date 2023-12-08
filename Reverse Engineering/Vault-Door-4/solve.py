decimals = "106 85 53 116 95 52 95 98"
decimals = decimals.split(" ")

hexadecimals = "0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f"
hexadecimals = hexadecimals.split(", ")

octals = "0142, 0131, 0164, 063, 0163, 0137, 0143, 061"
octals = octals.split(", ")

normal = '9' + '4' + 'f' + '7' + '4' + '5' + '8' + 'e'

flag = ""

for dec in decimals:
	flag += chr(int(dec))

for hexadecimal in hexadecimals:
	flag += bytearray.fromhex(hexadecimal[2:]).decode()

for octal in octals:
	flag += chr(int(octal[1:], 8))

print(flag+normal)