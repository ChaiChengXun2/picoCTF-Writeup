# Packets Primer - CTF Challenge Writeup

Challenge: Packets Primer
Points: 100
Category: Forensics

## Objective
The objective of the Packets Primer challenge is to familiarize yourself with the use of Wireshark, a popular network packet analysis tool. Your task is to uncover the hidden flag within a provided PCAP (Packet Capture) file.

## Solution
To successfully complete this challenge, follow these steps:

1. **Open the PCAP file**: Start by opening the provided PCAP file in Wireshark. Wireshark is a powerful tool for analyzing network packets and traffic.

2. **Multiple approaches**: There are various ways to solve this challenge, but a common approach is to follow the TCP stream.

3. **Follow TCP stream**: In Wireshark, you can follow the TCP stream. This will show you the content of the TCP packets in a more readable format.

4. **Find the flag**: Click through the TCP stream content by using the "Next" button or scrolling through the data. Eventually, you will discover the flag within the captured network traffic.

5. The flag format is `picoCTF{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you uncover during your analysis in Wireshark.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

Enjoy your exploration of Wireshark and network packet analysis, and happy hacking!
