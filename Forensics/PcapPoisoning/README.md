# PcapPoisoning - CTF Challenge Writeup

Challenge: PcapPoisoning
Points: 100
Category: Forensics

## Objective
The objective of the PcapPoisoning challenge is to perform network packet analysis on a pcap file to uncover the hidden flag. Your task is to navigate through the multitude of packets, identify relevant information, and find the flag.

## Solution
To successfully complete the PcapPoisoning challenge, follow these steps:

1. **Analyzing the Pcap File**:
   - The provided pcap file contains a vast number of network packets, making it necessary to inspect each one for potential clues.

2. **Unusual String**:
   - While analyzing the packets, you may come across a string that resembles base64 encoding. However, it is not actually the flag. 

3. **Packet Exploration**:
   - Examine each packet systematically, going through them one by one.
   - Keep a keen eye for any anomalies or unusual strings that might lead to the flag.

4. **Flag Discovery**:
   - By diligently analyzing the packets, you will eventually locate the flag hidden within one of them.

5. **Alternative Approach**:
   - If navigating through packets seems overwhelming, you can use the `strings` command to extract human-readable strings from the pcap file and search for "picoctf" within these strings:
     ```
     strings <pcap file> | grep -i "picoctf"
     ```

6. Following these steps, you will successfully unveil the hidden flag within the pcap file.

## Flag
The flag for this challenge is in the format: `picoCTF{XXXXXXXXXX}`.

In the PcapPoisoning challenge, you'll dive into network packet analysis and forensics to uncover the flag. Your careful examination of the packets will lead you to the hidden treasure. Good luck!
