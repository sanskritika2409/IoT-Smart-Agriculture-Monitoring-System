# 🌱 IoT-Enabled Smart Agriculture Monitoring System

## 📌 Project Overview

The IoT-Enabled Smart Agriculture Monitoring System is a smart farming solution designed to monitor environmental conditions in real time and automate irrigation decisions.

The system continuously tracks:

* Soil Moisture
* Temperature
* Humidity
* Light Intensity
* Water Level

Based on threshold values, the system generates alerts and controls irrigation systems automatically to reduce water wastage and improve crop productivity.

---

## 🎯 Problem Statement

Traditional farming relies heavily on manual monitoring of soil and environmental conditions. This often leads to:

* Excessive water consumption
* Delayed irrigation
* Crop stress
* Reduced productivity

This project solves these challenges using IoT-based monitoring and automation.

---

## 🚀 Features

### Real-Time Monitoring

* Soil Moisture Monitoring
* Temperature Monitoring
* Humidity Monitoring
* Light Intensity Monitoring
* Water Level Monitoring

### Smart Alerts

* Low Soil Moisture Alert
* High Temperature Alert
* Low Water Level Alert

### Automation

* Automatic Pump ON/OFF Logic
* Threshold-Based Irrigation

### Analytics

* CSV Data Logging
* Historical Trend Analysis
* Interactive Dashboard

### Dashboard

* Live Sensor Cards
* Gauge Meters
* Trend Charts
* Alert Center
* Download CSV Option

---

## 🛠️ Technology Stack

### Hardware

* ESP32 / Arduino UNO
* DHT22 Sensor
* Soil Moisture Sensor
* LDR Sensor
* Water Level Sensor
* Relay Module

### Software

* Python
* Streamlit
* Pandas
* Plotly
* Arduino IDE

### Simulation

* Wokwi
* Python Sensor Simulator

---

## 🏗️ Project Architecture

Sensors
↓
ESP32 / Simulation
↓
Data Processing
↓
Threshold Checking
↓
Alert Generation
↓
Dashboard Update
↓
Pump Control Logic
↓
CSV Data Logging

---

## 📂 Folder Structure

```text
IoT-Smart-Agriculture-Monitoring-System
│
├── arduino_code
├── python_simulation
├── dashboard
├── data
├── outputs
├── images
├── circuit_diagram
├── docs
├── README.md
├── requirements.txt
├── main.py
```

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/IoT-Smart-Agriculture-Monitoring-System.git

cd IoT-Smart-Agriculture-Monitoring-System

pip install -r requirements.txt
```

## ▶️ Run Project

Terminal 1

```bash
python main.py
```

Terminal 2

```bash
streamlit run python_simulation/dashboard.py
```

## 📈 Sample Output

```text
SMART AGRICULTURE MONITORING SYSTEM

Soil Moisture : 35%
Temperature : 38°C
Humidity : 70%
Light Intensity : 650
Water Level : 15%

ALERTS:
LOW SOIL MOISTURE ALERT
HIGH TEMPERATURE ALERT
LOW WATER LEVEL ALERT

PUMP STATUS: ON
```

## 📸 Screenshots

### Dashboard

images/dashboard.png
images/dashboard 1.png

### Sensor Trends

images/trends.png

### Alert Panel

images/alerts.png

### CSV Data

images/csv_output.png
# SERIAL monitor


images/serial_monitor.png
images/serial_monitor1.png



---

## 🎓 Learning Outcomes

* IoT Architecture Design
* Sensor Integration
* Dashboard Development
* Data Logging
* Automation Logic
* Smart Farming Concepts
* ESP32 Programming
* Python Development

---

## 💼 Industry Applications

* Precision Farming
* Smart Irrigation
* Greenhouse Monitoring
* Water Resource Management
* Agricultural Research

---

## 👨‍💻 Author

Sanskritika Awasthi

IoT | Embedded Systems | Data Analytics | Smart Agriculture
