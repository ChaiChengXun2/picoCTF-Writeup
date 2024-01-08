# Lookey Here

## Basic Information
- **Category**: Forensics
- **Difficulty**: Easy
- **Points**: 100

## Solving
The objective of this challenge is to demonstrate the effective use of the `grep` command to find specific text within a large file.

**Step 1: Large File**
- The challenge provides you with a large file that contains various data.

**Step 2: Using Grep**
- To find the flag, you can employ the `grep` command. `grep` is a powerful tool for searching text patterns in files.
- We suggest using the `-i` flag, which tells `grep` to ignore the case, making it case-insensitive.
- Run the following command to search for the flag within the file:
    ```shell
    cat <filename> | grep -i 'picoctf'
    ```

**Step 3: Find the Flag**
- After running the `grep` command, it will display any lines in the file containing the text 'picoCTF.'
- Locate the line with the flag and extract it.

**SOLVED**
Flag: picoCTF{XXXXXXXXXX}

By effectively using the `grep` command, you were able to search and locate the flag within the large file provided in the challenge. This exercise showcases the utility of command-line tools for text processing and searching.
