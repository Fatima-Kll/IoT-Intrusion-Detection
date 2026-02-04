# Results – Model Performance Overview

This folder presents the evaluation results of three learning approaches applied to **IoT Intrusion Detection**:

- Supervised Machine Learning  
- Unsupervised Anomaly Detection  
- Deep Learning  

---

## 🔹 Supervised Machine Learning

Five classical models were evaluated.

**Top performers**
- Random Forest, KNN, and Decision Tree  
- **100% accuracy** with very fast training times

**Lower performance**
- Logistic Regression and SVM struggled with complex traffic patterns

**Efficiency insight**
- SVM showed high computational cost, making it less suitable for real-time IoT environments

✅ **Tree-based models provide the best balance between accuracy and efficiency.**

---

## 🔹 Unsupervised Anomaly Detection

An MLP-based model was used to detect anomalies without labeled attacks.

- **Normal traffic**: Excellent detection (high recall)  
- **Anomalies**: High precision but lower recall  

⚠️ Reliable alerts, but conservative detection of subtle attacks.

---

## 🔹 Deep Learning (Multiclass Classification)

The deep learning model classifies multiple attack types across **MQTT and CoAP protocols**.

**Strong detection**
- MQTT normal traffic  
- UDP Flood  
- MQTT Publish Flood  

**Challenges**
- Confusion between similar MQTT attacks  
- Some CoAP flood traffic misclassified as normal

📌 Deep learning enables fine-grained attack classification and benefits from richer protocol-level features.

---

## 🚀 Key Takeaway

- **Machine Learning**: Fast, accurate, and reliable for known attacks  
- **Anomaly Detection**: Effective for detecting unknown behaviors  
- **Deep Learning**: Best suited for detailed, multi-attack classification  

