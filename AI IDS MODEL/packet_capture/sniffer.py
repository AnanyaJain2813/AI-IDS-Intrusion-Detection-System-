# Import sniff function from Scapy
from scapy.all import sniff
#snif - capture, analyze and manipulate network packets

# Import feature extractor
from packet_capture.feature_extractor import extract_features

# Import AI prediction function
from backend.predict import predict_attack

# Database session
from backend.database import SessionLocal
#it means:
#Create a new database session.
#Establish a connection to the database.Allow execution of queries (SELECT, INSERT, UPDATE, DELETE).
# #Manage transactions until the session is closed.

#database session is a temporary connection between an application (or user) and a database.

# Database model
from backend.model import Alert

# Current date/time
from datetime import datetime


# ==========================================
# RISK SCORE FUNCTION
# ==========================================

def calculate_risk(prediction):

    """
    Generate risk score
    based on prediction result
    """

    # Convert to lowercase for case-insensitive comparison
    prediction_lower = str(prediction).lower().strip()

    if prediction_lower == "normal":
        return 5

    elif prediction_lower == "dos":
        return 90

    elif prediction_lower == "probe":
        return 70

    elif prediction_lower == "r2l":
        return 85

    elif prediction_lower == "u2r":
        return 95

    else:
        # Log unexpected prediction values
        print(f"WARNING: Unknown prediction type: {prediction}")
        return 50


# ==========================================
# SAVE TO DATABASE
# ==========================================

def save_to_database(features, prediction, risk_score):

    db = SessionLocal()

    try:

        alert = Alert(

            source_ip=features["source_ip"],

            destination_ip=features["destination_ip"],
            
            protocol=features.get("protocol", "unknown"),
            
            packet_size=features.get("packet_size", 0),

            attack_type=str(prediction),

            risk_score=risk_score
        )

        db.add(alert)

        db.commit()

    except Exception as e:

        print("Database Error:", e)
        print(f"Failed to save alert at {datetime.now()}")

    finally:

        db.close()


# ==========================================
# PROCESS EACH PACKET
# ==========================================

def process_packet(packet):

    """
    Called every time
    a new packet arrives
    """

    try:

        # Extract features
        features = extract_features(packet)

        if features is None:
            return

        # Create ML data only
        ml_features = {}

        for key, value in features.items():

            if isinstance(key, int):
                ml_features[key] = value

        # Prediction
        prediction = predict_attack(ml_features)

        # Risk Score
        risk_score = calculate_risk(prediction)

        # Save in database
        save_to_database(
            features,
            prediction,
            risk_score
        )

        print("=" * 60)

        print("SOURCE IP :", features["source_ip"])

        print("DESTINATION IP :", features["destination_ip"])

        print("PREDICTION :", prediction)

        print("RISK SCORE :", risk_score)

        print("=" * 60)

    except Exception as e:

        print("Packet Processing Error:", e)


# ==========================================
# START SNIFFER
# ==========================================

def start_sniffer():

    print("\nStarting AI IDS...\n")

    sniff(
        prn=process_packet,
        store=False
    )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    start_sniffer()

#sniffer.py captures packets using Scapy.

# The packet is passed to extract_features()
# which converts packet information into
# model-compatible features.

# These features are passed to predict_attack()
# imported from predict.py.

# predict.py loads the trained Random Forest model
# and returns the prediction result.