"""
Pydantic schemas for data validation
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AlertCreate(BaseModel):
    """Schema for creating alerts"""
    source_ip: str
    destination_ip: str
    protocol: str
    packet_size: int
    attack_type: str
    risk_score: float

class AlertResponse(AlertCreate):
    """Schema for alert response"""
    id: int
    
    class Config:
        from_attributes = True

class PredictionRequest(BaseModel):
    """Schema for prediction requests"""
    source_ip: str
    destination_ip: str
    protocol: str
    packet_size: int
    transport_protocol: str
    source_port: int
    destination_port: int
    payload_length: int
    ttl: Optional[int] = 64
    tcp_flags: Optional[str] = None

class PredictionResponse(BaseModel):
    """Schema for prediction response"""
    prediction: str
    risk_score: float
    alert_id: Optional[int] = None

class SystemStats(BaseModel):
    """Schema for system statistics"""
    total_alerts: int
    alerts_today: int
    normal_packets: int
    malicious_packets: int
    false_positive_rate: Optional[float] = None
