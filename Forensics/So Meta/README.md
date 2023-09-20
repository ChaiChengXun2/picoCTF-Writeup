# So Meta - Forensics Writeup  

## Basic Information   
**Category:** Forensics    
**Points:** 150  

## Objective  

The "So Meta" challenge provides an opportunity to familiarize yourself with metadata extraction using the popular tool, ExifTool. The objective is to extract hidden information from an image file by inspecting its metadata.  

## Solution  

To successfully complete the "So Meta" challenge, follow these steps:  

Begin by downloading the image from the PicoCTF platform. This image contains hidden metadata that holds valuable information. Ensure that you have ExifTool installed on your local machine. ExifTool is a powerful command-line tool used for reading, writing, and manipulating image metadata.  

Open your terminal or command prompt and navigate to the directory where you downloaded the image. Then, run the following command to extract and display the image's metadata:  

```bash
exiftool image_filename
```  

Alternatively, if you don't have access to a Linux machine or ExifTool, you can use the [AperiSolve](https://www.aperisolve.com/) website to analyse the image and retrieve the hidden metadata.  

Upon inspecting the metadata, you will discover a hidden flag within the information. The flag is revealed as follows:  

Flag: picoCTF{XXXXXXXXXXXXXXXXXX}  

With this flag extracted from the image's metadata, you have successfully completed the "So Meta" challenge.  

**Challenge Solved**  
