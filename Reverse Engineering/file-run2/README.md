# file-run-2

## Basic Information
Category: Reverse Engineering  
Difficulty: Easy  
Points: 100  

## Solving
The objective of this challenge is to learn about file permissions (`chmod`) and running files with arguments.

**Step 1:**  
Download the provided file.

**Step 2:**   
Use the `chmod +x` command on the downloaded file to make it executable. This command changes the file permissions to allow execution.

```bash
chmod +x filename
```

**Step 3:**   
Run the file with ```Hello!``` as argument  
```
./run Hello!
```
