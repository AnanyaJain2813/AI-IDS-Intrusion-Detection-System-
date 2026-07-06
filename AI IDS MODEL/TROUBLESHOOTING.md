# 🔧 AI IDS - Troubleshooting Guide

## ✅ Fixed Issues

### Issue 1: "No module named uvicorn"
**Problem:** Dependencies not installed
**Solution:** 
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
python3 -m pip install -r requirements.txt
```
**Status:** ✅ FIXED - All dependencies installed

---

### Issue 2: "TemplateNotFound: dashboard.html"
**Problem:** Flask couldn't find templates in relative path
**Solution:** Updated frontend/app.py to use absolute paths
**Status:** ✅ FIXED - Flask app now loads correctly

---

## 🚀 How to Run (Updated)

### IMPORTANT: Install dependencies FIRST
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
python3 -m pip install -r requirements.txt
```

### Then run in 3 separate terminals:

**Terminal 1 - Backend API (Port 8000):**
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
python3 -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload
```
Expected output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

**Terminal 2 - Frontend Dashboard (Port 5000):**
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
python3 -m flask --app frontend.app run --host 0.0.0.0 --port 5000
```
Expected output:
```
Running on http://127.0.0.1:5000
```

**Terminal 3 - Packet Sniffer (requires sudo):**
```bash
cd "/Users/devrajsinghal/AI IDS MODEL"
sudo python3 packet_capture/sniffer.py
```
Expected output:
```
Starting AI IDS Packet Sniffer...
Connecting to API at: http://0.0.0.0:8000/api/predict
```

---

## ✅ Verification Checklist

- [ ] All dependencies installed (`python3 -m pip install -r requirements.txt`)
- [ ] Backend API running on http://localhost:8000
- [ ] Dashboard running on http://localhost:5000
- [ ] Sniffer running (with sudo)
- [ ] Dashboard loads without errors
- [ ] API documentation available at http://localhost:8000/docs

---

## 🔍 Testing the System

### 1. Check API Health
```bash
curl http://localhost:8000/api/health
```
Expected response: `{"status":"healthy","timestamp":"2026-06-02T..."}`

### 2. View Dashboard
Open browser to: http://localhost:5000

### 3. Check API Documentation
Open browser to: http://localhost:8000/docs

---

## ❌ Common Issues & Solutions

### "Port 8000 already in use"
**Solution:** Kill the process on that port or use a different port:
```bash
# Change port 8000 to 8001 in startup command:
python3 -m uvicorn backend.api:app --port 8001 --reload
```

### "Port 5000 already in use"
**Solution:** Kill the process on that port or use a different port:
```bash
# Change port 5000 to 5001 in startup command:
python3 -m flask --app frontend.app run --port 5001
```

### "Permission denied" for sniffer
**Solution:** Use sudo (administrator privileges required for packet capture):
```bash
sudo python3 packet_capture/sniffer.py
```

### Dashboard shows "Connecting..." status
**Solution:** 
1. Make sure Backend API (Terminal 1) is running on port 8000
2. Check http://localhost:8000/docs to verify API is responding

### Dashboard has no data
**Solution:**
1. Ensure Sniffer (Terminal 3) is running
2. Check that it's connected to http://localhost:8000/api/predict
3. Network traffic should be flowing for alerts to appear

---

## 📚 Documentation

- **QUICKSTART.md** - Quick start guide
- **README.md** - Full project overview
- **COMPLETION_STATUS.md** - Project completion details
- **API Docs** - Interactive at http://localhost:8000/docs

---

## ✨ System Status: ✅ READY

All issues have been fixed. The system is ready to run!

**Next Step:** Run the commands above in 3 separate terminals.
