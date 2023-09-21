# First Grep - General Skills Writeup

## Basic Information
**Category:** General Skills   
**Points:** 100  

## Objective

The "First Grep" challenge is designed to familiarize you with the `grep` command in a Linux environment. The goal is to use `grep` to search for specific text within a file.

## Solution

To successfully complete the "First Grep" challenge, follow these steps:

### Step 1: Use `grep` to Find the Flag

1. **Download and Cat the File:**
   - Begin by downloading the provided file.
   - Next, use the `cat` command to display the content of the file.
   - Pipe the output of `cat` into `grep` to search for the flag. The flag is typically surrounded by curly braces and contains the string "pico."

   ```bash
   cat file | grep "pico"
   ```  

Flag: picoCTF{XXXXXXX}  

**Challenge Solved**  
