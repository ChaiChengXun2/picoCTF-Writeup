# Extensions - Forensics Challenge

## Basic Information
- **Name:** Extensions
- **Category:** Forensics
- **Points:** 150

## Objective
The "Extensions" challenge aims to familiarize participants with different file formats and their extensions.

## Solution
Follow these steps to successfully solve the challenge:

1. **Download the File:**
   - Begin by downloading the provided file named `file.txt`.

2. **Identify File Format:**
   - Use the `file` command on the downloaded file to determine its file format.

3. **File Identified as PNG:**
   - Upon using the `file` command, you will observe that it identifies the file as a PNG image. This information is crucial.

4. **Inspect with Hex Editor & Check for Corruption:**
   - Use a hexadecimal editor (such as `hexedit`) to open and inspect the contents of the file.
   - In the hex editor, examine the file headers and ensure that they are not corrupted.

5. **Change File Extension:**
   - Based on the file format identified as PNG and that it is not corrupted, change the file extension from `file.txt` to `file.png`.

6. **Open the Image:**
   - Now that the file has been renamed to have a `.png` extension, you can open it as an image using an image viewer.
   - I use ```fim``` on linux to view images.

7. **Capture the Flag:**
   - Upon opening the image, you will find that it contains the hidden flag.

8. **Challenge Completed:**
   - You have successfully completed the "Extensions" challenge by identifying the true file format, renaming the file accordingly, and extracting the flag from the image.

## Flag
Congratulations! You've successfully completed the "Extensions" challenge and obtained the flag
