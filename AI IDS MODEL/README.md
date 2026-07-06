# AI Intrusion Detection System (AI IDS)

An AI-powered Intrusion Detection System (IDS) that captures live network traffic, extracts packet features, and detects malicious activities using Machine Learning. The system provides real-time threat detection, REST APIs, alert management, and a dashboard for monitoring suspicious network events.

---

## Features

- Real-time network packet capture using Scapy
- Machine Learning-based intrusion detection
- Automated feature extraction from network packets
- Threat classification (Normal / Malicious)
- Risk score generation for detected attacks
- REST API built with FastAPI
- SQLite database for alert storage
- Real-time alert management and statistics
- Interactive API documentation with Swagger UI

---

## Tech Stack

### Languages
- Python

### Frameworks
- FastAPI
- SQLAlchemy
- Uvicorn

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Networking & Security
- Scapy
- Network Packet Analysis
- Intrusion Detection System (IDS)

### Database
- SQLite

---

## Architecture

```
Network Traffic
        │
        ▼
 Packet Capture (Scapy)
        │
        ▼
 Feature Extraction
        │
        ▼
 Machine Learning Model
        │
        ▼
Attack Prediction
        │
        ▼
 Alert Storage (SQLite)
        │
        ▼
 FastAPI REST API
        │
        ▼
 Dashboard / Client
```

---

## Project Structure

```
AI-IDS/
│
├── backend/
│   ├── api.py
│   ├── database.py
│   ├── model.py
│   ├── predict.py
│   └── schemas.py
│
├── packet_capture/
│   ├── sniffer.py
│   └── feature_extractor.py
│
├── ml/
│   ├── ids_model.pkl
│   └── encoder.pkl
│
├── frontend/
├── database/
├── logs/
├── config.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/AnanyaJain2813/AI-IDS.git
cd AI-IDS
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Start Backend

```bash
uvicorn backend.api:app --reload
```

API Documentation

```
http://localhost:8000/docs
```

---

### Start Packet Capture

```bash
sudo python packet_capture/sniffer.py
```

---

## REST API

### Prediction

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/predict` | Predict malicious traffic |
| GET | `/api/health` | Health check |

### Alerts

| Method | Endpoint |
|---------|----------|
| GET | `/api/alerts` |
| GET | `/api/alerts/latest` |
| DELETE | `/api/alerts/{id}` |

### Statistics

| Method | Endpoint |
|---------|----------|
| GET | `/api/stats` |

---

## Workflow

1. Capture live network packets.
2. Extract network traffic features.
3. Send extracted features to the Machine Learning model.
4. Predict malicious or normal traffic.
5. Store malicious alerts in SQLite.
6. Retrieve alerts through FastAPI APIs.
7. Visualize security events on the dashboard.

---

## Database Schema

```
alerts
------
id
source_ip
destination_ip
protocol
packet_size
attack_type
risk_score
created_at
```

---

## Future Improvements

- SIEM Integration
- Microsoft Sentinel Integration
- Threat Intelligence APIs
- Email Alerting
- Docker Deployment
- Cloud Deployment (AWS)
- Deep Learning IDS
- Explainable AI (XAI)
- Real-time Dashboard Analytics

---

## Skills Demonstrated

- Machine Learning
- Network Security
- Intrusion Detection Systems (IDS)
- Python
- FastAPI
- REST APIs
- SQLAlchemy
- SQLite
- Scapy
- Feature Engineering
- Cybersecurity
- Threat Detection
- Secure Backend Development

---

## Author

**Ananya Jain**

Cybersecurity Enthusiast



## License

This project is licensed under the MIT License.
