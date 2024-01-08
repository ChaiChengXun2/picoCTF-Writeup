# tunn3l v1s10n - CTF Challenge Writeup

## Challenge Information
- **Name**: tunn3l v1s10n
- **Points**: 40
- **Category**: Forensics

## Objective
The objective of the "tunn3l v1s10n" CTF challenge is to develop skills in image forensics and to uncover a hidden flag within an image. You are presented with an unknown file and must determine its nature and extract the hidden flag. This challenge encourages participants to explore file headers, image analysis, and hex editing.

## Solution
To successfully complete the "tunn3l v1s10n" challenge, I followed these steps:

1. **Inspecting File Headers**:
   - When presented with an unknown file, it's often helpful to check for familiar headers or signatures that can hint at the file type.
   - In this case, I identified a `BM` signature, which indicated that the file is a bitmap image.

2. **Verification with `identify`**:
   - To double-check the file's format, I used the `identify` command to confirm that it was indeed a BMP image.


      ![Changing FIle Header](<hexedit for bmp.png>)

3. **Fixing the File Header**:
   - After correcting the header to fit a typical bitmap image, I was able to view the contents and found a fake flag.


      ![Fake Flag](<fake flag.png>)

4. **Noticing Cropped Image**:
   - I observed that the image on the very right was cut off, indicating that it might be part of the challenge.

5. **Exploring Image Dimensions**:
   - To address the image's cut-off section, I used `exiftool` to extract information about its width and height.
   - I identified the width and height values within the image's metadata.


      ![Image Dimensions](<image dimensions.png>)

6. **Hex Editing to Modify Dimensions**:
   - With the width and height values, I searched for the corresponding hex values in the image file and decided to modify them.
   - Initially, I doubled both the width and height, but that didn't yield the flag.
   - I then modified only the height value, doubling it, which resulted in the actual flag being revealed.


      ![Not Successful](<double width and height.png>)

      
      ![Real Flag](<real flag.png>)

By inspecting file headers, correcting the image's header, and exploring image dimensions through `exiftool` and hex editing, I successfully extracted the hidden flag for the "tunn3l v1s10n" challenge.

## Flag
The flag for this challenge is in the format `picoCTF{XXXXXXXXXX}`. Participants should follow the provided steps to analyze and modify the image file to uncover the hidden flag.

I hope this writeup offers guidance on how to approach and solve the "tunn3l v1s10n" CTF challenge. If you have any more questions or need further assistance, please feel free to ask.
