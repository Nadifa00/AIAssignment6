## Part 1: Theoretical Analysis

### Q1: Edge AI vs Cloud AI
Edge AI processes data locally on devices instead of sending it to the cloud.  
This **reduces latency** because decisions happen instantly without network delays, and **enhances privacy** since sensitive data stays on the device.  
**Example:** In autonomous drones, Edge AI enables real-time obstacle detection and navigation without needing an internet connection.

### Q2: Quantum AI vs Classical AI
**Classical AI** relies on traditional processors and sequential computation, while **Quantum AI** uses qubits that can represent multiple states simultaneously, allowing faster solutions to complex optimization problems.  
Industries that could benefit most include **finance** (portfolio optimization), **logistics** (route planning), **pharmaceuticals** (drug discovery), and **energy** (grid optimization).


## Part 2: Task 1 – Edge AI Prototype

![accuracy metrics](accuracy-metrics.png)

### How Edge AI Benefits Real-Time Applications
- **Low Latency:** Processes data instantly on the device without waiting for cloud responses.  
- **Privacy:** Sensitive data stays local, reducing security risks.  
- **Offline Functionality:** Works even without internet access.  
- **Reduced Bandwidth:** No need for continuous cloud communication.  
- **Energy Efficiency:** Lightweight models like TensorFlow Lite use less power, ideal for embedded systems.  
- **Real-Time Decision-Making:** Enables immediate responses in applications like smart cameras, autonomous vehicles, and IoT sensors.
  

# Task 2: AI-Driven IoT Concept – Smart Agriculture System

## Required Sensors
- **Soil Moisture Sensor** – Measures soil water level.  
- **Temperature Sensor (DHT11/DHT22)** – Monitors air temperature.  
- **Humidity Sensor** – Tracks air moisture levels.  
- **Light Sensor (LDR)** – Detects sunlight intensity.  
- **pH Sensor** – Checks soil acidity/alkalinity.  

## Proposed AI Model
- **Model Type:** Linear Regression or a small Neural Network  
- **Input Features:** Soil moisture, temperature, humidity, light, and pH values  
- **Output:** Predicted crop yield (in kg/hectare or yield percentage)  
- **Purpose:** Help farmers optimize irrigation and fertilizer usage for better productivity.
  
## Data Flow Diagram
[IoT Sensors]
(Soil, Temp, Humidity, Light, pH)
            ▼
[Microcontroller / Edge Device]
(e.g., Raspberry Pi or ESP32)
            ▼
[Data Preprocessing]
(Filtering, Normalization)
│          ▼
[AI Model]
(Predict Crop Yield)
│         ▼
[Dashboard / Cloud Display]

