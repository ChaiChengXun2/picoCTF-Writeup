# Matryoshka Doll - CTF Challenge Writeup

Challenge: Matryoshka Doll
Points: 30
Category: Forensics

## Objective
The objective of the Matryoshka Doll challenge is to learn about discovering files hidden within other files. Your task is to unveil the hidden flag within a provided image file.

## Solution
To successfully complete this challenge, follow these steps:

1. **Examine the image file**: Start by examining the provided image file. At first glance, it may appear to be a normal image, but pay attention to the file's size.

2. **Large file size**: You may notice that the file size of the image is unusually large for a simple image, which is a hint that there could be hidden content.

3. **Use Binwalk**: To reveal files hidden within files, you can use a tool called `binwalk` on Linux. Binwalk is specifically designed for analyzing and extracting hidden files within binary files.

4. Run the following command: `binwalk -e <image_filename>`. This command tells binwalk to extract all hidden files within the image.

5. Once you run this command, binwalk will extract the hidden files and display them in a separate directory. Navigate to the extracted files.

6. Continue extracting any images you find within the extracted images until you discover the flag.

7. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you uncover during your exploration of the nested files.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Enjoy your journey into uncovering hidden files within files, and happy hacking!
