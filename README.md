# AI Intrusion Detection System (AI IDS)

An AI-powered Intrusion Detection System (IDS) that captures live network traffic, extracts network features, and detects malicious activities using Machine Learning. The system provides real-time threat detection, REST APIs, alert management, and a web dashboard for monitoring security events.

---

## Features

- Real-time packet capture using **Scapy**
- Machine Learning-based intrusion detection
- Live network feature extraction
- Threat classification with risk scoring
- FastAPI REST API
- Interactive web dashboard
- SQLite database for alert management
- REST APIs for alerts, statistics, and predictions
- Modular backend architecture
- Swagger API documentation

---

## Tech Stack

### Languages
- Python
- HTML
- CSS
- JavaScript

### Frameworks & Libraries
- FastAPI
- SQLAlchemy
- Uvicorn
- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Security & Networking
- Scapy
- Intrusion Detection System (IDS)
- Network Packet Analysis

### Database
- SQLite

---

# Project Structure

```text
AI-IDS-Intrusion-Detection-System/
│
├── backend/                       # FastAPI Backend
│   ├── api.py                     # REST API endpoints
│   ├── database.py                # Database configuration
│   ├── model.py                   # SQLAlchemy models
│   ├── predict.py                 # ML prediction engine
│   └── schemas.py                 # API schemas
│
├── frontend/                      # Web Dashboard
│   ├── app.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │       ├── alerts.js
│   │       ├── dashboard.js
│   │       └── statistics.js
│   │
│   └── templates/
│       ├── dashboard.html
│       ├── alerts.html
│       ├── statistics.html
│       └── 404.html
│
├── packet_capture/                # Packet Capture Engine
│   ├── sniffer.py
│   └── feature_extractor.py
│
├── ml/                            # Machine Learning Models
│   ├── ids_model.pkl
│   └── encoder.pkl
│
├── database/
│   └── ids.db
│
├── logs/
│   └── alerts.log
│
├── data/                          # Dataset
│
├── config.py
├── main.py
├── requirements.txt
├── start.sh
├── STARTUP.sh
├── README.md
├── QUICKSTART.md
├── TROUBLESHOOTING.md
├── ISSUES_FIXED.md
└── COMPLETION_STATUS.md
```

---

# System Architecture

```text
                Live Network Traffic
                        │
                        ▼
             Packet Capture (Scapy)
                        │
                        ▼
             Feature Extraction Engine
                        │
                        ▼
           Machine Learning Prediction
                        │
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
   Normal Traffic             Malicious Traffic
         │                             │
         ▼                             ▼
      Ignore                   Store Alert (SQLite)
                                      │
                                      ▼
                             FastAPI Backend API
                                      │
                                      ▼
                          Dashboard & REST Endpoints
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/AnanyaJain2813/AI-IDS-Intrusion-Detection-System.git
```

Move into the project directory

```bash
cd AI-IDS-Intrusion-Detection-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

### Start Backend API

```bash
uvicorn backend.api:app --reload
```

API Documentation

```
http://localhost:8000/docs
```

Swagger UI

```
http://localhost:8000/redoc
```

---

### Start the Dashboard

```bash
python frontend/app.py
```

---

### Start Packet Capture

```bash
sudo python packet_capture/sniffer.py
```

---

# API Endpoints

## Prediction

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/predict` | Predict malicious traffic |
| GET | `/api/health` | Health status |

---

## Alerts

| Method | Endpoint |
|---------|----------|
| GET | `/api/alerts` |
| GET | `/api/alerts/latest` |
| DELETE | `/api/alerts/{id}` |

---

## Statistics

| Method | Endpoint |
|---------|----------|
| GET | `/api/stats` |

---

# Workflow

1. Capture live network packets using Scapy.
2. Extract packet features for machine learning.
3. Predict malicious or normal traffic.
4. Generate a risk score.
5. Store detected threats in SQLite.
6. Expose alerts through FastAPI APIs.
7. Visualize threats on the dashboard.

---

# Skills Demonstrated

- Intrusion Detection Systems (IDS)
- Machine Learning
- Python
- FastAPI
- REST APIs
- SQLAlchemy
- SQLite
- Network Security
- Packet Analysis
- Scapy
- Feature Engineering
- Threat Detection
- Backend Development
- Cybersecurity
- API Development

---

# Future Improvements

- Microsoft Sentinel Integration
- SIEM Integration
- Docker Deployment
- AWS Deployment
- Threat Intelligence APIs
- Email Alerting
- Explainable AI (XAI)
- Deep Learning-based IDS

---

# Author

**Ananya Jain**

Cyber Security Enthusiast

- LinkedIn: https://www.linkedin.com/in/ananya-jain-715b9b29a/
- GitHub: https://github.com/AnanyaJain2813

---

# License

Licensed under the MIT License.
