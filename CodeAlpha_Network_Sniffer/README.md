# CodeAlpha_Network_Sniffer

## Project Overview

This project is a Python-based **Basic Network Sniffer** developed as part of the Cyber Security Internship at **CodeAlpha**. The tool captures live network traffic packets and analyzes their structure to demonstrate how data flows across a network and to explore the foundational concepts of internet protocols.

---

## Features

- **Packet Interception:** Captures raw IPv4 network packets using socket programming.
- **Header Parsing:** Unpacks the first 20 bytes of intercepted packets to extract critical routing information.
- **Data Extraction:** Accurately isolates and displays:
  - Source and Destination IP addresses
  - Time to Live (TTL)
  - Header Length and Total Length
  - Identification and Fragment Offsets
- **Protocol Identification:** Translates protocol numbers into human-readable formats (e.g., TCP, UDP, ICMP).
- **Payload Extraction:** Isolates and displays the underlying data payload from the network routing headers.

---

## Prerequisites

To run this script, you will need:

- **Python 3.x** installed on your machine.
- **Administrator/Root Privileges:** Raw sockets require elevated permissions to intercept traffic directly from the network interface.

---

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/CodeAlpha_Network_Sniffer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CodeAlpha_Network_Sniffer
   ```

3. Run the script with administrator privileges:

   **Windows** (Command Prompt / PowerShell as Admin):
   ```cmd
   python sniffer.py
   ```

   **Linux / macOS** (Terminal):
   ```bash
   sudo python3 sniffer.py
   ```

4. The terminal will display the parsed header information and payload for the first captured packet, then safely exit and disable promiscuous mode.

---

## Disclaimer

This script was created strictly for **educational purposes** and cybersecurity training as part of the CodeAlpha internship program. It should only be used in controlled, local environments or networks where you have **explicit permission** to monitor traffic. Unauthorized interception of network traffic is illegal and unethical.

---

## Author

**[Adesina Ayomide]** — Cybersecurity Intern at CodeAlpha
