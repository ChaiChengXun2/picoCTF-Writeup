# First Find - General Skills Writeup

## Basic Information
**Category:** General Skills  
**Points:** 100

## Objective

The "First Find" challenge is designed to help you familiarize yourself with the `grep` tool in a Linux environment. The objective is to efficiently search for specific keywords within a large collection of files and directories.

## Solution

To successfully complete the "First Find" challenge, follow these steps:

1. **Download and Unzip the File:**
   - Download the provided file from the PicoCTF platform.
   - Unzip the downloaded file to access its contents.

2. **Explore the Contents:**
   - Upon unzipping the file, you'll likely find numerous files, folders, and sub-folders.
   - Instead of manually searching through each of them, we'll utilize the power of the `grep` tool.

3. **Use `grep` with Recursive Search:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you unzipped the file.
   - Use the `grep` command with the `-r` (or `--recursive`) option to search for a specific keyword across all files and subdirectories within the current directory.
   - Additionally, use the `-i` option to make the search case-insensitive. This means that "picoCTF" will match "picoctf" and similar variations.
   - Here's the command:
     ```bash
     grep -r -i "picoctf"
     ```  
   - Running this command will search for the keyword "picoCTF" throughout all the files and subdirectories in the current directory and its subdirectories.

4. **Retrieve the Flag:**
   - After executing the `grep` command, look for instances where the keyword "picoCTF" is found.
   - The flag will be in the format `picoCTF{XXXXXXX}`.

With this approach, you can efficiently search for the flag without manually examining each file and folder individually.

Flag: `picoCTF{XXXXXXX}`

**Challenge Accomplished**
