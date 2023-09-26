# St3g0 - Steganography Challenge

## Basic Information
- **Name:** St3g0
- **Category:** Steganography
- **Points:** 300

## Objective
The "St3g0" challenge aims to educate participants about steganography and the use of the least significant bit (LSB) to hide information within an image.

## Solution
Follow these steps to successfully solve the challenge:

1. **Examine the Image:**
   - Begin by examining the provided image file. It appears to be a regular image, but there might be hidden information.

2. **Use zsteg Tool:**
   - To extract hidden data from the image, we can use the `zsteg` tool.
   - Run the following command to analyze the image and filter for LSB data:
     ```
     zsteg -a --lsb <filename>
     ```

3. **Identify the Flag:**
   - After running the `zsteg` command, it will filter and extract the LSB data from the image.
   - Carefully examine the extracted data to find the flag hidden within the LSB.

4. **Capture the Flag:**
   - You will find that the extracted LSB data contains the hidden flag.

5. **Challenge Completed:**
   - Congratulations! You have successfully completed the "St3g0" challenge by using `zsteg` to identify and extract the LSB-hidden flag from the image.

## Flag
Well done! You've successfully completed the "St3g0" steganography challenge and obtained the flag
