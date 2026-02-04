Results – Model Performance Overview

This folder contains the evaluation results of three learning approaches applied to IoT intrusion detection:

Supervised Machine Learning

Unsupervised Anomaly Detection

Deep Learning

🔹 Supervised Machine Learning

Five classical models were evaluated.

Best Performers:
Random Forest, KNN, and Decision Tree achieved 100% accuracy with very fast training times.

Lower Performance:
Logistic Regression and SVM struggled with complex traffic patterns.

Efficiency Insight:
SVM showed a high computational cost, making it less suitable for real-time IoT environments.

✅ Tree-based models offer the best balance between accuracy and efficiency.

🔹 Anomaly Detection (Unsupervised)

An MLP-based model was used to detect anomalies without labeled attacks.

Normal traffic: Excellent detection (high recall).

Anomalies: High precision but lower recall, meaning the model is cautious and may miss subtle attacks.

⚠️ Reliable alerts, but conservative detection.

🔹 Deep Learning (Multiclass)

The deep learning model classifies multiple attack types across MQTT and CoAP protocols.

Strong detection: MQTT normal traffic, UDP Flood, MQTT Publish Flood.

Challenges: Confusion between similar MQTT attacks and some CoAP floods classified as normal traffic.

📌 Deep learning enables fine-grained attack classification but benefits from richer protocol features.

🚀 Key Takeaway

ML: Fast, accurate, and reliable for known attacks

Anomaly Detection: Useful for unknown behaviors

Deep Learning: Best for detailed, multi-attack classification
