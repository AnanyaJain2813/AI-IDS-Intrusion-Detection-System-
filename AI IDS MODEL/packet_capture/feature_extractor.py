"""
Extract ML-ready features from network packets using Scapy
"""
from scapy.all import IP, TCP, UDP, ICMP
import struct

def extract_features(packet):
    """
    Extract network features from packet for ML model
    Returns dict with feature names and values
    """
    try:
        # Check if packet has IP layer
        if not packet.haslayer(IP):
            return None
        
        ip_layer = packet[IP]
        features = {}
        
        # IP layer features
        features['source_ip'] = ip_layer.src
        features['destination_ip'] = ip_layer.dst
        features['protocol'] = ip_layer.proto
        features['packet_size'] = len(packet)
        features['ttl'] = ip_layer.ttl
        
        # Check transport layer (TCP/UDP/ICMP)
        if packet.haslayer(TCP):
            tcp_layer = packet[TCP]
            features['transport_protocol'] = 'TCP'
            features['source_port'] = tcp_layer.sport
            features['destination_port'] = tcp_layer.dport
            features['tcp_flags'] = tcp_layer.flags
            features['sequence_number'] = tcp_layer.seq
            features['acknowledgment'] = tcp_layer.ack
            features['window_size'] = tcp_layer.window
            
        elif packet.haslayer(UDP):
            udp_layer = packet[UDP]
            features['transport_protocol'] = 'UDP'
            features['source_port'] = udp_layer.sport
            features['destination_port'] = udp_layer.dport
            features['udp_length'] = udp_layer.len
            
        elif packet.haslayer(ICMP):
            icmp_layer = packet[ICMP]
            features['transport_protocol'] = 'ICMP'
            features['icmp_type'] = icmp_layer.type
            features['icmp_code'] = icmp_layer.code
            
        else:
            features['transport_protocol'] = 'OTHER'
            features['source_port'] = 0
            features['destination_port'] = 0
        
        # Payload analysis
        payload = packet.payload
        if payload:
            features['payload_length'] = len(str(payload))
        else:
            features['payload_length'] = 0
        
        return features
        
    except Exception as e:
        print(f"[ERROR] Feature extraction failed: {e}")
        return None
