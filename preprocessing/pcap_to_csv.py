"""
PCAP to CSV Preprocessing Script

This script processes CSV files generated from PCAP traffic captures
and extracts flow-based features for IoT intrusion detection.

Used in the IoT Intrusion Detection project.
PCAP files and full datasets are not included in this repository.
"""

import pandas as pd

# ========================
# Configuration
# ========================

INPUT_CSV = "input_attack.csv"      # CSV extracted from PCAP (example)
OUTPUT_CSV = "output_flows.csv"     # Processed flow-based dataset
LABEL = "MQTT_Publish_Flood"        # Traffic label

# ========================
# Load CSV
# ========================

df = pd.read_csv(INPUT_CSV)

# ========================
# Port Handling (TCP / UDP)
# ========================

for col in ['tcp.srcport', 'tcp.dstport', 'udp.srcport', 'udp.dstport']:
    if col not in df.columns:
        df[col] = 0
    df[col] = df[col].fillna(0).astype(int)

# Unified source and destination ports
df['src_port'] = df['tcp.srcport'].where(df['tcp.srcport'] != 0, df['udp.srcport'])
df['dst_port'] = df['tcp.dstport'].where(df['tcp.dstport'] != 0, df['udp.dstport'])

# ========================
# Flow Aggregation (5-tuple)
# ========================

flows = df.groupby(['ip.src', 'ip.dst', 'src_port', 'dst_port', 'ip.proto'])

flow_data = flows.agg(
    flow_duration=('frame.time_epoch', lambda x: x.max() - x.min()),
    num_packets=('frame.len', 'count'),
    total_bytes=('frame.len', 'sum'),
    min_pkt_size=('frame.len', 'min'),
    max_pkt_size=('frame.len', 'max'),
    mean_pkt_size=('frame.len', 'mean')
).reset_index()

# ========================
# Labeling
# ========================

flow_data['label'] = LABEL

# ========================
# Save Output
# ========================

flow_data.to_csv(OUTPUT_CSV, index=False)

print("✅ Flow-based CSV dataset generated successfully.")
