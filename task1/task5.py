from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        if proto == 6:  # TCP Protocol
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif proto == 17:  # UDP Protocol
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol = "Other"
            src_port = "N/A"
            dst_port = "N/A"
        
        print(f"IP {ip_src}:{src_port} -> {ip_dst}:{dst_port} | Protocol: {protocol}")
        
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload) if packet.haslayer(TTCP) else bytes(packet[UDP].payload)
            print(f"Payload: {payload}\n")
    else:
        print("Non-IP packet detected\n")

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
