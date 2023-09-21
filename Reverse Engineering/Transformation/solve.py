import codecs

def main():
	with open("enc") as file: 
		lines = file.readlines()

		answer = ""

		for char in lines[0]:
			answer += hex(ord(char))[2:]

	flag = codecs.decode(answer, "hex").decode("ASCII")  
	print(flag)

main()
