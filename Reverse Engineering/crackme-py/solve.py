def main():
    password = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"

    answer = ""

    for letter in password:
        if ord(letter) + 47 < 127:
            answer += chr(ord(letter) + 47)
        else:
            answer += chr(ord(letter) + 47 - 94)

    print(answer)

main()
