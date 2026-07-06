# 🚀 AI IDS - Quick Start Guide

Your complete AI Intrusion Detection System is now ready! Follow these steps to get it running.

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Elevated privileges (for packet capture)

## 1️⃣ Installation

### Step 1: Install Dependencies
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
pip install -r requirements.txt
```

### Step 2: Verify Installation
```bash
python3 -c "import fastapi; import flask; import scapy; print('✓ All dependencies installed')"
```

## 2️⃣ Running the System

You need to run **three separate terminals**:

### Terminal 1: Start FastAPI Backend
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
python3 -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload
```
✅ Backend will be available at: **http://localhost:8000**
📚 API Docs: **http://localhost:8000/docs**

### Terminal 2: Start Flask Frontend Dashboard
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
python3 -m flask --app frontend.app run --host 0.0.0.0 --port 5000
```
✅ Dashboard available at: **http://localhost:5000**

### Terminal 3: Start Packet Sniffer (requires sudo)
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
sudo python3 packet_capture/sniffer.py
```

> **Note:** Scapy requires administrator/root privileges to capture packets.
> You'll be prompted to enter your password.

## 🎯 System Flow

```
Network Traffic
       ↓
   [Sniffer] ← captures packets using Scapy
       ↓
[Feature Extractor] ← extracts ML features (IP, port, protocol, etc.)
       ↓
 [ML Predictor] ← runs trained model (ids_model.pkl)
       ↓
    [Alert DB] ← stores malicious detections
       ↓
  [REST API] ← exposes via FastAPI endpoints
       ↓
 [Web Dashboard] ← visualizes threats in real-time
```

## 📊 Using the Dashboard

Once all three services are running, open **http://localhost:5000** in your browser.

### Main Dashboard
- **Real-time stats** on normal vs. malicious traffic
- **Live alerts** table with latest detections
- **Charts** showing traffic patterns
- **System health** indicator

### Alerts Page (`/alerts`)
- View all captured alerts with full details
- Filter by time period and risk level
- Pagination for browsing large datasets
- Delete individual or bulk alerts

### Statistics Page (`/statistics`)
- Comprehensive analytics and trends
- Traffic composition charts
- Top attacking source IPs
- Export data as CSV or JSON
- Print detailed reports

## 🔧 API Endpoints

### Make Predictions
```bash
curl -X POST "http://localhost:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "source_ip": "192.168.1.1",
    "destination_ip": "10.0.0.1",
    "protocol": "TCP",
    "packet_size": 1500,
    "transport_protocol": "TCP",
    "source_port": 54321,
    "destination_port": 443,
    "payload_length": 1460,
    "ttl": 64
  }'
```

### Get Alerts
```bash
curl "http://localhost:8000/api/alerts?skip=0&limit=10"
```

### Get Statistics
```bash
curl "http://localhost:8000/api/stats"
```

### Health Check
```bash
curl "http://localhost:8000/api/health"
```

## 📁 Project Structure

```
AI IDS MODEL/
├── backend/                          # FastAPI REST API
│   ├── api.py                       # Main endpoints
│   ├── database.py                  # SQLAlchemy setup
│   ├── model.py                     # Alert ORM model
│   ├── predict.py                   # ML inference
│   └── schemas.py                   # Request/response schemas
│
├── frontend/                         # Flask web dashboard
│   ├── app.py                       # Flask routes
│   ├── templates/                   # HTML templates
│   │   ├── dashboard.html           # Main dashboard
│   │   ├── alerts.html              # Alerts page
│   │   ├── statistics.html          # Stats page
│   │   └── 404.html                 # Error page
│   └── static/                      # Static assets
│       ├── css/style.css            # Styling
│       └── js/
│           ├── dashboard.js         # Dashboard logic
│           ├── alerts.js            # Alerts logic
│           └── statistics.js        # Stats logic
│
├── packet_capture/
│   ├── sniffer.py                   # Packet capture
│   └── feature_extractor.py         # Feature extraction
│
├── ml/
│   ├── ids_model.pkl                # Trained ML model
│   └── encoder.pkl                  # Label encoder
│
├── database/                         # SQLite database (auto-created)
├── logs/                            # System logs
├── config.py                        # Configuration
├── requirements.txt                 # Python dependencies
└── README.md                        # Full documentation
```

## 🛠️ Troubleshooting

### "Permission denied" when running sniffer
**Solution:** Use `sudo` and enter your password when prompted.

### Port 8000 or 5000 already in use
**Solution:** Change the port in the command:
```bash
# For backend (change 8000 to 8001)
python3 -m uvicorn backend.api:app --port 8001

# For frontend (change 5000 to 5001)
python3 -m flask --app frontend.app run --port 5001
```

### ImportError: No module named 'fastapi'
**Solution:** Run `pip install -r requirements.txt` again.

### Dashboard shows "Connecting..."
**Solution:** Make sure the backend API is running on port 8000.

### No alerts being captured
**Solution:** 
1. Ensure sniffer is running with sudo
2. Check network traffic on your system
3. Verify ML model file exists at `ml/ids_model.pkl`

## 📈 Next Steps

1. **Customize alerting**: Add email/Slack notifications in `backend/api.py`
2. **Improve detection**: Retrain ML model with your own dataset
3. **Add authentication**: Implement user login for dashboard
4. **Deploy**: Use Docker for containerization
5. **Monitor**: Set up 24/7 monitoring with alerts

## 📞 Support

For issues or questions:
- Check API documentation at: http://localhost:8000/docs
- Review logs in the `logs/` directory
- Examine database: `database/ids.db` (SQLite)

---

**Ready to detect threats in real-time! 🛡️**
