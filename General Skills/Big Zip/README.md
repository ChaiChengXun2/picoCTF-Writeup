# Big Zip - General Skills Challenge

## Basic Information
**Name:** Big Zip  
**Category:** General Skills  
**Points:** 100

## Objective

The "Big Zip" challenge aims to test my general skills, particularly my ability to extract data from a large compressed archive.

## Solution

This is how I approached and solved the "Big Zip" general skills challenge:

1. **Unzip the File:**
   - My first step was to unzip the file provided for the challenge. It was described as a "big zip," so I anticipated that it contained a large number of files.

2. **Explore the Unzipped Files:**
   - After unzipping the file, I noticed that it had indeed expanded into a directory with many files.

3. **Use `grep` to Search for the Flag:**
   - To locate the flag, I used the `grep` command with the `-r` option to search recursively and the `-i` option for a case-insensitive search. My goal was to search through all files within the directory for the string "picoCTF."
     - The command I used was: `grep -r -i 'picoCTF'`.

4. **Flag Discovery:**
   - After running the `grep` command, I identified a file containing the text "picoCTF," and this led me to the flag.

Flag: picoCTF{XXXXXXXXXX}

**Challenge Solved**  
