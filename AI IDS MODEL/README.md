# AI Intrusion Detection System (IDS) with Machine Learning

A complete ML-powered network intrusion detection system that captures packets, extracts features, and predicts malicious traffic in real-time.

## 🏗️ Project Structure

```
AI IDS MODEL/
├── backend/              # FastAPI REST backend
│   ├── api.py           # REST endpoints
│   ├── database.py      # SQLAlchemy ORM setup
│   ├── model.py         # Alert database model
│   ├── predict.py       # ML inference
│   └── schemas.py       # Data validation
├── frontend/            # Web dashboard (Phase 2)
│   └── app.py
├── packet_capture/      # Network packet capture
│   ├── sniffer.py       # Main packet sniffer
│   └── feature_extractor.py  # Feature extraction for ML
├── ml/                  # Machine learning models
│   ├── ids_model.pkl    # Trained model
│   └── encoder.pkl      # Label encoder
├── database/            # SQLite database (auto-created)
├── logs/                # System logs
├── config.py            # Configuration
└── requirements.txt     # Python dependencies
```

## 📦 Installation

1. **Clone the repository:**
```bash
cd /Users/devrajsinghal/AI\ IDS\ MODEL
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### Step 1: Start the Backend API
```bash
python3 -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Step 2: Start the Packet Sniffer (requires sudo)
```bash
sudo python3 packet_capture/sniffer.py
```

## 📡 API Endpoints

### Predictions
- **POST** `/api/predict` - Predict if traffic is malicious
- **GET** `/api/health` - Health check

### Alerts
- **GET** `/api/alerts` - Get all alerts
- **GET** `/api/alerts/latest?hours=24` - Get recent alerts
- **DELETE** `/api/alerts/{alert_id}` - Delete alert

### Statistics
- **GET** `/api/stats` - System statistics

## 🔄 System Flow

1. **Packet Capture**: Scapy sniffer captures network packets
2. **Feature Extraction**: Extracts ML-ready features (IP, ports, protocol, payload, etc.)
3. **Prediction**: Sends features to ML model → Returns normal/malicious label
4. **Alert Storage**: Malicious predictions stored in SQLite database
5. **API Access**: Retrieve alerts and stats via REST API
6. **Dashboard**: Web UI visualizes threats in real-time (Phase 2)

## 📊 Database Schema

**alerts** table:
```sql
CREATE TABLE alerts (
    id INTEGER PRIMARY KEY,
    source_ip STRING,
    destination_ip STRING,
    protocol STRING,
    packet_size INTEGER,
    attack_type STRING,
    risk_score FLOAT,
    created_at DATETIME
)
```


## 📄 License

MIT License

## 👤 Author

Developed by ANANYA JAIN.
