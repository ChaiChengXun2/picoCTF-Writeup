# CTF Challenge Writeup
**Name:** shark on wire 1
**Points:** 150
**Category:** Forensics

## Objective

The objective of this challenge is to analyze network traffic and locate the flag hidden within the captured packets.

## Solution

1. **Analyzing the Protocol Hierarchy**
   - To get started, my first step was to analyze the protocol hierarchy within the captured network traffic. This helps identify which protocols are in use and may provide a hint on where to focus.

2. **Investigating UDP Traffic**
   - Upon closer examination, it became apparent that most of the network traffic was in the form of UDP (User Datagram Protocol) packets. With this observation in mind, I decided to start by analyzing the UDP traffic.

3. **Exploring the UDP Stream**
   - Focusing on the UDP stream, I dug deeper into the data. It's within the contents of the UDP packets that the flag is concealed. Your task is to navigate the UDP stream and uncover the hidden flag.

4. **Flag Discovery**
   - As you explore the UDP stream, you will eventually find the flag. It may be split across multiple packets or hidden within the data, so careful inspection is required.

## Flag
The flag for the shark on wire 1 challenge is `picoCTF{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag you find while investigating the UDP stream.

Congratulations on completing this Forensics challenge! You've demonstrated your skills in analyzing network traffic and locating hidden information within captured packets.
