# Magikarp Ground Mission - CTF Challenge Writeup

Challenge: Magikarp Ground Mission
Points: 30
Category: General Skills

## Objective
The objective of the Magikarp Ground Mission is to learn about basic SSH and Linux commands.

## Solution
To successfully complete this challenge, follow these steps:

1. **SSH into the instance provided to you**: You will be given SSH access to an instance where the challenge is hosted. You can use the `ssh` command to connect to this instance. Here's an example command:

        ```ssh username@hostname -p port```

Replace `username`, `hostname`, and `port` with the provided credentials.

2. **Use `cat`, `ls`, and `cd` to complete the challenge**: Once you are connected to the instance, navigate through the directories and use the following commands:
- `cat`: Use this command to view the contents of files.
- `ls`: Use this command to list the files and directories in the current directory.
- `cd`: Use this command to change directories.

3. **Read the instruction.txt files**: At each directory you navigate to, look for an `instruction.txt` file. These files will provide you with hints or instructions on what to do next. You should read these files carefully to progress in the challenge.

4. As you follow the instructions, you will eventually find the flag. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you need to find.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Good luck, and happy hacking!
