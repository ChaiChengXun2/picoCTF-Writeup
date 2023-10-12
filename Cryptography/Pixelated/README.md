# Pixelated - CTF Challenge Writeup

Challenge: Pixelated
Points: 100
Category: Cryptography

## Objective
The objective of the Pixelated challenge is to learn about Visual Cryptography and how to decode a flag hidden within two distorted images.

## Solution
To successfully complete this challenge, follow these steps:

1. **Examine the images**: Initially, both image appears distorted and not reveal any flag.

2. **Use common cryptography tools**: Traditional tools such as ```zsteg``` and ```exiftool``` may not be helpful in revealing the flag.

3. **Hint about stacking images**: The challenge hints at stacking images and provides links to Visual Cryptography. Visual Cryptography involves splitting images into multiple parts to prevent people from reading the original content.

4. **Combine both images**: To solve this challenge, you need to combine both distorted images to reveal the flag. One way to do this is by using the "ADD" operand in stegsolve.

5. **Use Stegsolve**: Open one of the images in stegsolve and navigate to the "Image Combiner" tool. Use the "ADD" operand to combine the two images.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Happy exploration of Visual Cryptography, and happy hacking!
