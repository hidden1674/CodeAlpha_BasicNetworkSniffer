# CodeAlpha Basic Network Sniffer

A basic network packet sniffer developed in Python using the Scapy library as part of the CodeAlpha Cyber Security Internship.

## 📌 Project Overview

This project captures and analyzes network packets from the local system.

The sniffer displays useful information about captured IP packets, including:

* Source IP address
* Destination IP address
* Protocol
* Source port
* Destination port
* Packet size
* Payload sample
* Packet timestamp

The program also provides final traffic statistics for different protocols.

## 🛠️ Technologies Used

* Python
* Scapy
* Npcap
* VS Code

## 📂 Project Structure

```text
CodeAlpha_BasicNetworkSniffer/
│
├── sniffer.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Install the required Python package

```bash
python -m pip install -r requirements.txt
```

### 2. Run the network sniffer

```bash
python sniffer.py
```

The program will start capturing network packets.

Press `Ctrl+C` to stop the capture and display the final traffic statistics.

## 📊 Information Captured

For each IP packet, the program displays:

```text
Time
Source IP
Destination IP
Protocol
Source Port
Destination Port
Packet Size
Payload Sample
```

The supported protocols include:

* TCP
* UDP
* ICMP
* Other IP protocols

## 📈 Traffic Statistics

After stopping the program, the sniffer displays:

* Total IP packets
* Total TCP packets
* Total UDP packets
* Total ICMP packets
* Total packets classified as Other

## 🎯 Learning Objectives

This project helped me understand:

* How network packets are structured
* Basic network traffic analysis
* IP addresses and ports
* TCP, UDP and ICMP protocols
* Packet capture using Scapy
* Basic Python programming for cybersecurity
* How packet sniffers work

## ⚠️ Ethical & Security Note

This tool should only be used on networks and devices that you own or have explicit permission to monitor.

Network packets may contain sensitive information. This project displays only a limited payload sample and does not save captured packets to a file.

## 👨‍💻 Internship

**CodeAlpha Cyber Security Internship**

**Task:** Basic Network Sniffer
