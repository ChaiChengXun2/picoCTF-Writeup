scrambled_password = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
password = [None] * 32

i = 0

while i < 8:
	password[i] = scrambled_password[i]
	i += 1

while i < 16:
	password[i] = scrambled_password[23 - i]
	i += 1

while i < 32:
	password[i] = scrambled_password[46 - i]
	i += 2

i = 31
while i >= 17: 
	password[i] = scrambled_password[i]
	i -= 2

print(f"{''.join(password)}")