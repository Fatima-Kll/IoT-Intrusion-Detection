# Dataset Description

## 1. Overview

This dataset was generated locally as part of a final-year project focused on
IoT intrusion detection in MQTT and CoAP-based environments.

The traffic represents both **normal behavior** and **malicious activity**
targeting IoT communication protocols.

All data was generated in a controlled laboratory environment using
simulated IoT devices and attack scripts.

---

## 2. Data Source

- Network traffic was captured using **Wireshark**
- Traffic was generated using:
  - MQTT broker (Mosquitto)
  - CoAP server
  - Custom attack scripts
- Attacks were launched from a local machine against the IoT services

The raw data was initially captured in **PCAP format**.

---

## 3. PCAP Availability

Due to the large size of PCAP files and GitHub storage limitations,
**raw PCAP files are not included in this repository**.

Instead, the PCAP files were:

1. Processed locally
2. Converted to CSV format
3. Cleaned and merged into a single dataset used for machine learning

This approach ensures reproducibility while keeping the repository lightweight.

---

## 4. Attack Types Included

The dataset includes the following traffic categories:

### Normal Traffic

- Legitimate MQTT publish/subscribe messages
- Legitimate CoAP requests

### Malicious Traffic

- MQTT Publish Flood
- MQTT Crafted Packet Attack
- MQTT Authentication Bypass
- TCP Flood
- UDP Flood
- CoAP Crafted Payload Attack
- CoAP PUT Flood

Each traffic sample is labeled to distinguish between normal and attack behavior.

TCP SYN flooding traffic was generated during IoT-Flock-based experiments and used for dataset labeling. The script is provided for academic illustration only.

---

## 5. Feature Extraction

From the network traffic, several features were extracted, including:

- Packet size
- Protocol type
- Source and destination ports
- Time-based features
- Flow-related statistics

These features were selected to support both:

- Classical Machine Learning algorithms
- Deep Learning models

---

## 6. Dataset Usage

The dataset is used for:

- Intrusion detection experiments
- Machine Learning model training and evaluation
- Anomaly detection
- Deep Learning experiments

The dataset serves as the foundation for the experimentation phase of this project.

---

## 7. Reproducibility

All steps for:

- Traffic generation
- Attack execution
- Data preprocessing

are documented in their respective folders in this repository, allowing
the dataset to be regenerated if needed.
