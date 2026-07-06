#!/bin/bash
# AI IDS System - Startup Instructions

echo "🛡️ AI IDS System - Startup Guide"
echo "=================================="
echo ""

# Step 1: Install dependencies (one time)
echo "Step 1: Installing dependencies (one time only)..."
python3 -m pip install -r requirements.txt
echo "✅ Dependencies installed!"
echo ""

# Instructions for running
echo "Step 2: Run these commands in SEPARATE TERMINALS:"
echo ""
echo "=========================================="
echo "Terminal 1 - Backend API:"
echo "=========================================="
echo "python3 -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload"
echo ""
echo "=> Access API at: http://localhost:8000"
echo "=> API Documentation: http://localhost:8000/docs"
echo ""

echo "=========================================="
echo "Terminal 2 - Web Dashboard:"
echo "=========================================="
echo "python3 -m flask --app frontend.app run --host 0.0.0.0 --port 5000"
echo ""
echo "=> Access Dashboard at: http://localhost:5000"
echo ""

echo "=========================================="
echo "Terminal 3 - Packet Sniffer (requires sudo):"
echo "=========================================="
echo "sudo python3 packet_capture/sniffer.py"
echo ""
echo "=> Captures network packets and sends to backend"
echo "=> You will be prompted for your password"
echo ""

echo "=========================================="
echo "📊 System Status:"
echo "=========================================="
echo "Once all 3 are running:"
echo "✓ Dashboard: http://localhost:5000"
echo "✓ API Docs: http://localhost:8000/docs"
echo "✓ Sniffer: Capturing packets..."
echo ""
