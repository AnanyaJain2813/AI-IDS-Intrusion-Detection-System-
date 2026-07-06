"""
Configuration settings for AI IDS
"""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATABASE_DIR = PROJECT_ROOT / "database"
ML_DIR = PROJECT_ROOT / "ml"

# Ensure directories exist
DATABASE_DIR.mkdir(exist_ok=True)

# Database settings
DATABASE_URL = "sqlite:///./database/ids.db"
DATABASE_TIMEOUT = 30

# FastAPI settings
API_HOST = "0.0.0.0"
API_PORT = 8000
API_RELOAD = True

# Packet sniffer settings
SNIFFER_INTERFACE = None  # Auto-detect interface
PACKET_COUNT = 0  # Sniff indefinitely

# ML model paths
MODEL_PATH = str(ML_DIR / "ids_model.pkl")
ENCODER_PATH = str(ML_DIR / "encoder.pkl")

# Alert settings
RISK_THRESHOLD = 50.0  # Risk score threshold for alerts
ALERT_LOG_FILE = "logs/alerts.log"

# Create logs directory
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(exist_ok=True)
