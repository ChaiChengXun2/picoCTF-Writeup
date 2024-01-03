# Repetitions - CTF Challenge Writeup

Challenge: Repetitions
Points: 100
Category: General Skills

## Objective
The objective of the Repetitions challenge is to learn about base64 encoding and decoding. Your task is to decode a message that has been encoded multiple times and discover the hidden flag.

## Solution
To successfully complete this challenge, follow these steps:

1. **Understand the repetition**: As suggested by the challenge name, the encrypted text is encoded multiple times. Your goal is to decode the message iteratively to reveal the flag.

2. **Decode the message**: Start by decoding the message once. If the flag is not yet revealed, continue decoding it multiple times, following the same encoding pattern.

3. You may notice that the encoding pattern is base64, and decoding the message using base64 repeatedly will help uncover the hidden flag.

4. Keep decoding the message until you reveal the flag.

5. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discover during the iterative decoding process.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Enjoy your exploration of base64 encoding and the repetitive decoding process, and happy hacking!
