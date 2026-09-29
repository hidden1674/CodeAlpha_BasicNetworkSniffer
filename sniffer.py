from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


# Total packet count
packet_count = 0

# Protocol statistics
protocol_stats = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "Other": 0
}


def analyze_packet(packet):
    global packet_count

    # Process only packets containing IP
    if IP not in packet:
        return

    packet_count += 1

    # Get IP addresses
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    # Identify protocol and ports
    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"
        source_port = "N/A"
        destination_port = "N/A"

    else:
        protocol = "Other"
        source_port = "N/A"
        destination_port = "N/A"

    # Update protocol statistics
    protocol_stats[protocol] += 1

    # Packet size
    packet_size = len(packet)

    # Current time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Display packet information
    print("\n" + "=" * 60)
    print(f"PACKET #{packet_count}")
    print("=" * 60)

    print("Time             :", timestamp)
    print("Source IP        :", source_ip)
    print("Destination IP   :", destination_ip)
    print("Protocol         :", protocol)
    print("Source Port      :", source_port)
    print("Destination Port :", destination_port)
    print("Packet Size      :", packet_size, "bytes")

    # Display payload sample if available
    if Raw in packet:
        payload = bytes(packet[Raw].load)

        # Show only first 40 bytes
        print("Payload Sample   :", repr(payload[:40]))
    else:
        print("Payload Sample   : No payload available")


def show_statistics():
    print("\n")
    print("=" * 60)
    print("             TRAFFIC STATISTICS")
    print("=" * 60)

    print("Total IP Packets :", packet_count)
    print()

    print("TCP Packets      :", protocol_stats["TCP"])
    print("UDP Packets      :", protocol_stats["UDP"])
    print("ICMP Packets     :", protocol_stats["ICMP"])
    print("Other Packets    :", protocol_stats["Other"])

    print("=" * 60)


# Program starting message
print("=" * 60)
print("             CODEALPHA BASIC NETWORK SNIFFER")
print("=" * 60)
print("Capturing network packets...")
print("Open a website or use the internet to generate traffic.")
print("Press Ctrl+C to stop.")
print()


try:

    # Start packet capture
    sniff(
        prn=analyze_packet,
        store=False
    )

except KeyboardInterrupt:

    print("\nStopping packet capture...")

    # Show final statistics
    show_statistics()