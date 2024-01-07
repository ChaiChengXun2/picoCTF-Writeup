# MacroHard WeakEdge - Forensics Challenge

## Basic Information
**Name:** MacroHard WeakEdge  
**Category:** Forensics  
**Points:** 60

## Objective

The "MacroHard WeakEdge" challenge introduces you to the world of digital forensics, focusing on Microsoft PowerPoint files. Your objective is to uncover a hidden flag within a PowerPoint file by employing various forensics techniques.

## Solution

To successfully complete the "MacroHard WeakEdge" challenge, follow these steps:

1. **Examine the PowerPoint File:**
   - Begin by opening the given PowerPoint file. At first glance, it may seem like a standard presentation.

2. **Use Binwalk for File Extraction:**
   - Microsoft files, including PowerPoint presentations, can hide secrets within. Use a tool like `binwalk` to extract hidden content.

3. **Extract Hidden Data:**
   - Run `binwalk` on the PowerPoint file to extract any embedded files or data. This step aims to uncover concealed information that is not immediately visible.

4. **Search for the Flag:**
   - After extracting the hidden data, you can use `grep` to search for specific keywords that may hint at the flag. Keep in mind that the flag may be encoded, so be prepared to decode it.

5. **Locate the Suspicious File:**
   - While searching through the extracted files, keep an eye out for any suspiciously named files, especially one named "hidden."

6. **View and Decode the Hidden File:**
   - Once you find the "hidden" file, open and examine its contents. This file likely contains the encoded flag. Your task is to decode it to reveal the actual flag.

Flag: picoCTF{XXXXXXXXXX}

**Challenge Solved**  
