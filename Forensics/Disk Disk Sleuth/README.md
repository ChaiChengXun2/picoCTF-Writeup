# Disk, disk, sleuth! - CTF Challenge Writeup

Challenge: Disk, disk, sleuth!
Points: 110
Category: Forensics

## Objective
The objective of the Disk, disk, sleuth! challenge is to introduce participants to the field of disk analysis and forensic investigation. Your task is to explore the contents of a disk image and uncover the hidden flag using forensic tools and techniques.

## Solution
To successfully complete the Disk, disk, sleuth! challenge, follow these steps:

1. **Introduction to Disk Analysis**:
   - Understand that this challenge serves as an introduction to disk analysis and forensic investigation, making it a suitable starting point for those new to the field.

2. **Using Autopsy**:
   - Autopsy, a digital forensics platform, is a commonly used tool for such challenges. You'll use it to open and analyze the disk image.

3. **Manual Analysis**:
   - Once you have the disk image opened in Autopsy, you can manually examine its contents, look for hidden information, or recover deleted files.

4. **Keyword Search**:
   - For this specific challenge, the solution is relatively straightforward. Instead of an in-depth manual analysis, I performed a keyword search.
   - I searched for keywords related to the CTF challenge on the disk image using Autopsy's search functionality.
   - I set the search to be case-insensitive, allowing for flexibility in finding potential flags.

5. **Discovering the Flag**:
   - After running the keyword search, the tool will highlight or list all instances of the specified keywords. Look through the search results, and you'll discover the flag.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

In the Disk, disk, sleuth! challenge, the use of forensic tools like Autopsy simplifies the process of uncovering the flag hidden within the disk image. Good luck!
