"""
AI IDS Main Orchestrator
Runs all system components together (when manually executed)
For production use, run each component in separate terminal as shown in QUICKSTART.md
"""
import subprocess
import time
import os
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent

def check_dependencies():
    """Check if all required packages are installed"""
    print("[1/3] Checking dependencies...")
    try:
        import fastapi
        import flask
        import scapy
        import sqlalchemy
        print("✓ All dependencies installed\n")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Install with: pip install -r requirements.txt\n")
        return False

def start_backend():
    """Start FastAPI backend"""
    print("[2/3] Starting FastAPI backend on http://localhost:8000")
    try:
        cmd = [sys.executable, "-m", "uvicorn", "backend.api:app", 
               "--host", "0.0.0.0", "--port", "8000", "--reload"]
        process = subprocess.Popen(cmd, cwd=PROJECT_DIR)
        time.sleep(3)
        print("✓ Backend started (PID: {})\n".format(process.pid))
        return process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}\n")
        return None

def start_frontend():
    """Start Flask frontend"""
    print("[3/3] Starting Flask frontend on http://localhost:5001")
    try:
        cmd = [sys.executable, "-m", "flask", "--app", "frontend.app", 
               "run", "--host", "0.0.0.0", "--port", "5001"]
        process = subprocess.Popen(cmd, cwd=PROJECT_DIR)
        time.sleep(2)
        print("✓ Frontend started (PID: {})\n".format(process.pid))
        return process
    except Exception as e:
        print(f"❌ Failed to start frontend: {e}\n")
        return None

def main():
    """Main orchestrator"""
    print("\n" + "="*50)
    print("🛡️  AI IDS System Orchestrator")
    print("="*50 + "\n")

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Start services
    backend_process = start_backend()
    frontend_process = start_frontend()

    if not backend_process or not frontend_process:
        print("❌ Failed to start services")
        sys.exit(1)

    # Print info
    print("="*50)
    print("✅ Services Started!")
    print("="*50)
    print("\n📊 Dashboard:  http://localhost:5001")
    print("📚 API Docs:   http://localhost:8000/docs")
    print("🔍 API Base:   http://localhost:8000")
    
    print("\n⚠️  To start the packet sniffer, open another terminal and run:")
    print("   sudo python3 packet_capture/sniffer.py")
    
    print("\n💡 Press Ctrl+C to stop all services...\n")

    try:
        # Keep running
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n\n⏹️  Shutting down services...")
        backend_process.terminate()
        frontend_process.terminate()
        time.sleep(1)
        backend_process.kill()
        frontend_process.kill()
        print("✓ All services stopped\n")

if __name__ == "__main__":
    main()
