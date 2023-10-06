character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
encrypted_flag = "128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"

# Split the encrypted flag into individual numbers
encrypted_flag = encrypted_flag.split(" ")

flag = ""

# Decrypt each number using mod 37 and map it to the character set
for item in encrypted_flag:
    flag += character_set[int(item) % 37]

print(flag)