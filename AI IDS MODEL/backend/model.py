from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from backend.database import Base

class Alert(Base):
    """Alert database table - stores malicious traffic detections"""
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String, index=True)
    destination_ip = Column(String, index=True)
    protocol = Column(String)
    packet_size = Column(Integer)
    attack_type = Column(String)
    risk_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
