"""
FastAPI backend for AI IDS
Handles predictions, alert logging, and statistics
"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import func

from backend.database import SessionLocal, engine, Base
from backend.schemas import AlertCreate, AlertResponse, PredictionRequest, PredictionResponse, SystemStats
from backend.model import Alert
from backend.predict import predict_attack
from packet_capture.feature_extractor import extract_features

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="AI IDS API",
    description="Intrusion Detection System with Machine Learning",
    version="1.0.0"
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============ PREDICTION ENDPOINT ============
@app.post("/api/predict", response_model=PredictionResponse)
def predict_attack_endpoint(request: PredictionRequest, db: Session = Depends(get_db)):
    """
    Predict if a packet is normal or malicious
    """
    try:
        # Prepare data for ML model
        input_data = {
            'protocol': request.protocol,
            'packet_size': request.packet_size,
            'transport_protocol': request.transport_protocol,
            'source_port': request.source_port,
            'destination_port': request.destination_port,
            'payload_length': request.payload_length,
            'ttl': request.ttl,
            'tcp_flags': request.tcp_flags if request.tcp_flags else 'none'
        }
        
        # Get ML prediction (returns 0 for normal, 1 for malicious)
        prediction_value = predict_attack(input_data)
        
        # Determine attack type and risk score
        attack_type = "Malicious" if prediction_value == 1 else "Normal"
        risk_score = 85.0 if prediction_value == 1 else 15.0
        
        # Store alert in database if malicious
        alert_id = None
        if prediction_value == 1:
            alert = Alert(
                source_ip=request.source_ip,
                destination_ip=request.destination_ip,
                protocol=request.protocol,
                packet_size=request.packet_size,
                attack_type=attack_type,
                risk_score=risk_score
            )
            db.add(alert)
            db.commit()
            db.refresh(alert)
            alert_id = alert.id
        
        return PredictionResponse(
            prediction=attack_type,
            risk_score=risk_score,
            alert_id=alert_id
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

# ============ ALERTS ENDPOINT ============
@app.get("/api/alerts", response_model=list[AlertResponse])
def get_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all stored alerts with optional pagination
    """
    alerts = db.query(Alert).offset(skip).limit(limit).all()
    return alerts

@app.get("/api/alerts/latest")
def get_latest_alerts(hours: int = 24, db: Session = Depends(get_db)):
    """
    Get alerts from the last N hours
    """
    cutoff_time = datetime.utcnow() - timedelta(hours=hours)
    alerts = db.query(Alert).filter(Alert.created_at >= cutoff_time).all()
    return alerts

@app.delete("/api/alerts/{alert_id}")
def delete_alert(alert_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific alert
    """
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    db.delete(alert)
    db.commit()
    return {"message": "Alert deleted"}

# ============ STATISTICS ENDPOINT ============
@app.get("/api/stats", response_model=SystemStats)
def get_stats(db: Session = Depends(get_db)):
    """
    Get system statistics
    """
    total_alerts = db.query(func.count(Alert.id)).scalar()
    
    # Alerts from today
    today = datetime.utcnow().date()
    alerts_today = db.query(func.count(Alert.id)).filter(
        func.date(Alert.created_at) == today
    ).scalar()
    
    # Count by prediction type
    malicious_count = db.query(func.count(Alert.id)).filter(
        Alert.risk_score >= 50
    ).scalar()
    normal_count = total_alerts - malicious_count if total_alerts else 0
    
    return SystemStats(
        total_alerts=total_alerts or 0,
        alerts_today=alerts_today or 0,
        normal_packets=normal_count,
        malicious_packets=malicious_count or 0,
        false_positive_rate=None
    )

# ============ HEALTH CHECK ============
@app.get("/api/health")
def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

# ============ ROOT ENDPOINT ============
@app.get("/")
def root():
    """
    API root endpoint with documentation link
    """
    return {
        "message": "AI IDS API is running",
        "docs": "/docs",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
