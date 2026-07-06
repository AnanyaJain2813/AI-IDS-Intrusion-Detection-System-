#!/bin/bash
# Startup script for AI IDS System

echo "🛡️ Starting AI IDS System..."
echo ""

PROJECT_DIR="/Users/devrajsinghal/AI IDS MODEL"
cd "$PROJECT_DIR"

# Check if dependencies are installed
echo "[1/3] Checking dependencies..."
python3 -c "import fastapi; import flask; import scapy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Dependencies not installed. Installing now..."
    pip install -r requirements.txt
    echo "✓ Dependencies installed"
else
    echo "✓ Dependencies already installed"
fi

echo ""
echo "🚀 Starting AI IDS Services..."
echo ""

# Start backend API
echo "[2/3] Starting FastAPI backend on http://localhost:8000"
python3 -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!
sleep 3

# Start frontend
echo "[3/3] Starting Flask frontend on http://localhost:5000"
python3 -m flask --app frontend.app run --host 0.0.0.0 --port 5000 &
FRONTEND_PID=$!
sleep 2

echo ""
echo "✅ Services Started!"
echo ""
echo "📊 Dashboard: http://localhost:5000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "⚠️ To start the packet sniffer, open another terminal and run:"
echo "   sudo python3 packet_capture/sniffer.py"
echo ""
echo "Press Ctrl+C to stop all services..."
echo ""

# Wait for services
wait $BACKEND_PID $FRONTEND_PID
