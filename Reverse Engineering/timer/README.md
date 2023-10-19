# Timer - Reverse Engineering Challenge

## Basic Information
**Name:** Timer  
**Category:** Reverse Engineering  
**Points:** 100

## Objective

The "Timer" challenge is a reverse engineering task that involves analyzing an Android application to find the flag. Your objective is to explore the application's code to locate the hidden flag.

## Solution

To successfully complete the "Timer" reverse engineering challenge, follow these steps:

1. **Use JADX-GUI for Android Reversing:**
   - For Android application reversing, it's common to use tools like JADX-GUI. This tool allows you to decompile and analyze the code of Android apps.

2. **Open the Application File:**
   - Open the provided Android application file using JADX-GUI. Once opened, you can access the decompiled code of the app.

3. **Investigate the "com" Folder:**
   - In Android app decompilation, custom code is typically found within the ```com``` folder. Navigate to the ```com``` folder to explore the app's source code.

        ![COM Folder](<com folder.png>)

1. **Examine the Main Activity:**
   - Start your investigation by examining the ```Main Activity``` file. This is often a good place to look for relevant code.

2. **Search for Clues:**
   - I did not find the flag within the ```Main Activity``` file, so I used the search feature from JADX-GUI to search for the flag
![Flag](<search feature.png>)

1. **Flag Retrieval:**
   - Once you've located the flag within the code, you've successfully completed the challenge.

Flag: picoCTF{XXXXXXXXXX}

**Challenge Solved**  
