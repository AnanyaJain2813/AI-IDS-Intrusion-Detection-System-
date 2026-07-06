import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load trained AI IDS model
model = joblib.load("ml/ids_model.pkl")


def predict_attack(data):

    # Convert input dictionary into dataframe
    df = pd.DataFrame([data])

    # Convert text/string columns into numeric values
    # ML model only understands numbers
    for col in df.columns:

        # Check if column datatype is object/string
        if df[col].dtype == 'object':

            # Create temporary label encoder
            le = LabelEncoder()

            # Convert strings into numbers
            # Example:
            # tcp -> 0
            # udp -> 1
            df[col] = le.fit_transform(df[col].astype(str))

    # Predict attack using trained model
    prediction = model.predict(df)

    # Return prediction result
    return prediction[0]