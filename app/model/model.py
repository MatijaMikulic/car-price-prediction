import joblib
from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve(strict=True).parent

path_model = f"{BASE_DIR}/random_forest_regressor_model.pkl"
path_scaler=f"{BASE_DIR}/scaler.pkl"
path_encoder=f"{BASE_DIR}/df_encoded.pkl"

with open(path_model,"rb") as f:
    model = joblib.load(f)

with open(path_scaler,"rb") as f:
    scaler = joblib.load(f)

with open(path_encoder,"rb") as f:
    encoder = joblib.load(f)

def predict(car):
    input = pd.DataFrame([car.dict()])
    input_encoded = pd.get_dummies(input, columns=["manufacturer", "model", "condition", "cylinders", "transmission", "drive"])

    # Reorder columns
    input_encoded = input_encoded.reindex(columns=encoder.columns)

    # Scale numeric features
    input_encoded[['odometer','age']] = scaler.transform(input_encoded[['odometer', 'age']])

    input_encoded=input_encoded.drop(['price'],axis=1)
    input_encoded.fillna(0, inplace=True)

    print(input_encoded)

    predicted_price = model.predict(input_encoded)
    return int(predicted_price)

    

    