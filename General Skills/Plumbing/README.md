# CTF Challenge Writeup
**Name:** Plumbing
**Points:** 200
**Category:** General Skills

## Objective

The objective of this challenge is to connect to a remote server instance using Netcat (nc) and use command-line pipes to search for a specific flag format.

## Solution

1. **Connecting to the Remote Server**
   - To tackle this challenge, you need to connect to a remote server instance provided via Netcat (nc). Netcat is a versatile networking utility that allows you to establish connections to servers.

2. **Using Pipes and Grep**
   - Once you've connected to the remote server, your goal is to search for a specific flag format that includes "picoctf."

3. **Command Syntax**
   - The command to achieve this can be as simple as using a pipe "|" to send the output of the remote server to the `grep` command. The `-i` option for `grep` is used to perform a case-insensitive search.

4. **Executing the Command**
   - The command for this purpose can be as follows:
     ```
     nc jupiter.challenges.picoctf.org 7480 | grep -i "picoctf"
     ```
   - This command connects to the specified remote server and pipes the output to `grep`, which searches for the string "picoctf" in a case-insensitive manner.

5. **Flag Discovery**
   - Upon executing the command, you will retrieve the flag that matches the specified format. This flag is what you need to complete the challenge.

## Flag
The flag for the Plumbing challenge is `picoCTF{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag you obtain after executing the provided command and finding the correct flag format.

Congratulations on completing this General Skills challenge! You've demonstrated your proficiency in using Netcat and command-line pipes to search for specific patterns in data.
