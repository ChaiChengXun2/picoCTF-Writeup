import hashlib
from cryptography.fernet import Fernet
import base64

username_trial = b"PRITCHARD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"

first_letter = hashlib.sha256(username_trial).hexdigest()[4]
second_letter = hashlib.sha256(username_trial).hexdigest()[5]
third_letter = hashlib.sha256(username_trial).hexdigest()[3]
fourth_letter = hashlib.sha256(username_trial).hexdigest()[6]
fifth_letter = hashlib.sha256(username_trial).hexdigest()[2]
sixth_letter = hashlib.sha256(username_trial).hexdigest()[7]
seventh_letter = hashlib.sha256(username_trial).hexdigest()[1]
eighth_letter = hashlib.sha256(username_trial).hexdigest()[8]

print(f"{key_part_static1_trial}{first_letter}{second_letter}{third_letter}{fourth_letter}{fifth_letter}{sixth_letter}{seventh_letter}{eighth_letter}{key_part_static2_trial}")