# Fresh Java - Reverse Engineering Challenge

## Basic Information
**Name:** Fresh Java  
**Category:** Reverse Engineering  
**Points:** 200

## Objective

The "Fresh Java" challenge in the Reverse Engineering category focuses on Java class files. The objective is to reverse engineer the Java code to find the flag.

## Solution

Here's how you can approach and solve the "Fresh Java" reverse engineering challenge:

1. **Initial Examination:**
   - When you download the challenge file, you will notice that it's a Java class file (usually with the `.class` extension).

2. **Java Decompilation:**
   - To explore and decompile the Java class, you can use a tool like `jd-gui`. JD-GUI is a popular Java decompiler that can convert compiled Java class files back into readable Java code.
   - Open the `jd-gui` application and load the Java class file into it.

3. **Analyzing the Decompiled Code:**
   - Once the Java class file is loaded, you'll see the decompiled Java code.
   - In this code, there might be multiple functions, but focus on the part where the flag is being checked.
   - Look for `if` statements, loops, or any other control structures that handle the flag.

4. **Flag Extraction:**
   - In the code, you will find the flag being checked letter by letter in various `if` statements or other similar structures.
   - You can use Python or any scripting language to dynamically extract the flag based on the conditions specified in the code.
    ```python
    flag = ""

    with open("text.txt", "r") as file:
      content = file.readlines() 

      for line in content:
        line = line[:-1].strip()
        flag += line[-3]

    print(flag[::-1])
    ```

By following this approach, you can reverse engineer the Java class file to extract the flag.

**Challenge Solved**

Flag: picoCTF{XXXXXXXXXX}
