# IoT Intrusion Detection Project

## 📌 Project Overview 

This project focuses on detecting malicious activities in Internet of Things (IoT) environments using Machine Learning (ML) and Deep Learning (DL) techniques.

The work is based on generating **normal and attack traffic** in an IoT environment using MQTT and CoAP protocols.  
Traffic generation was performed using the **IoT-Flock framework**, which was configured and executed locally to simulate realistic IoT environments.

The generated traffic was captured, processed into a dataset, and used to train Machine Learning and Deep Learning models for intrusion detection.

This project was developed as a **final academic project**.


## Key Contributions
- Local generation of labeled IoT attack traffic (MQTT & CoAP)
- Creation of a reproducible intrusion detection dataset
- Comparative evaluation of ML, anomaly detection, and Deep Learning models
- Analysis of protocol-specific attack detection challenges


 --- 


## 🎯 Objectives 

- Generate realistic IoT network traffic 
- Simulate multiple IoT-based attacks 
- Capture and preprocess network traffic 
- Build a labeled intrusion detection dataset 
- Apply Machine Learning and Deep Learning models 
- Evaluate and compare model performance

## 🏗 System Architecture The system includes: 
- MQTT broker (Mosquitto) 
- CoAP server 
- IoT traffic and attack generators 
- Traffic capture using Wireshark 
- Dataset creation and preprocessing 
- ML and DL-based intrusion detection models Architecture diagram is available in: 

architecture/system_architecture_MQTT.png

architecture/system_architecture_CoAP.png

## 🔧 Traffic Generation with IoT-Flock

IoT-Flock was used as a traffic generation framework to simulate realistic IoT environments and produce both normal and malicious network traffic.

The framework was configured and executed locally to:
- Generate MQTT and CoAP traffic
- Simulate different attack scenarios
- Produce PCAP files for dataset creation

Only the generated traffic and datasets were used in this project.  
The IoT-Flock source code is **not included** in this repository.


## 📂 Project Structure 
IoT-Intrusion-Detection/ 

├── architecture/ # System architecture diagram 

├── coap/ # CoAP server implementation 

├── mqtt/ # Mosquitto broker configuration 

├── attack-scripts/ # IoT attack scripts 

├── preprocessing/ # PCAP to CSV and dataset processing
 
├── data/ # Sample dataset and description
 
├── ml/ # Machine Learning models 

├── dl/ # Deep Learning models 

├── results/ # Evaluation results and figures 

└── .gitignore # Ignored files


## ⚔ Simulated Attacks 

The following attacks were implemented:
 - MQTT Publish Flood
 - MQTT Authentication Bypass 
 - CoAP PUT Flood 
 - TCP and UDP flooding (during traffic generation) Each attack script is located in:
 attack-scripts/


## 📊 Dataset 

- Traffic was captured in **PCAP format** - Converted to **CSV files** - Labeled as *normal* or *attack*
- The dataset is not included in this repository due to size and security considerations.
- All steps for traffic generation, preprocessing, and dataset construction are documented to ensure reproducibility 
- 📁 Dataset file:  data/data_description.md

> dataset and PCAP files are not included for size and security reasons.

 ---

 ## 🤖 Machine Learning & Deep Learning

Classical supervised Machine Learning models were evaluated to detect known attacks.

Unsupervised Machine Learning techniques were applied for anomaly detection to identify unknown or abnormal traffic patterns.

Deep Learning models were implemented for multiclass attack classification across MQTT and CoAP protocols.

Model performance was evaluated using accuracy, precision, recall, and confusion matrices.

📁 Notebooks: 

ml/ml_models.ipynb 

dl/deep_learning_model.ipynb 

--- 

## 📈 Results Model evaluation results and figures are available in: 
results/ 


---



## 🛠 Technologies Used 

- IoT-Flock
- Python
- MQTT (Mosquitto)
- CoAP
- Wireshark
- Scikit-learn
- TensorFlow / Keras
- Jupyter Notebook


--- 


 ## ▶ How to Run

1. Install the required dependencies:

pip install -r requirements.txt

2. (Optional) Generate traffic and attacks:

Run IoT traffic or attack scripts as needed.

3. Preprocess the captured traffic:

Use the preprocessing scripts to convert PCAP files into CSV datasets.

4. Train and evaluate models:

Open and run the Jupyter notebooks in the ml/ and dl/ folders.

⚠ Disclaimer 

This project is for academic and research purposes only. 

Attack scripts are provided strictly for educational use. 


👤 Author Fatima Zahra Final Year Project – IoT Security & Artificial Intelligence
