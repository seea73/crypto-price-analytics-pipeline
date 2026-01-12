import pandas as pd
import numpy as np
import os

BRONZE_PATH = "data/bronze/bitcoin_prices_raw.csv"
SILVER_PATH = "data/silver"
os.makedirs(SILVER_PATH, exist_ok=True)

def preprocess_data():
    # Load bronze data
    df = pd.read_csv(BRONZE_PATH, parse_dates=["timestamp"])

    # Sort by time
    df = df.sort_values("timestamp")

    # Remove duplicates
    df = df.drop_duplicates()

    # Set timestamp as index
    df.set_index("timestamp", inplace=True)

    # Handle missing prices
    df["price"] = df["price"].interpolate(method="time")

    # Create daily returns
    df["return"] = df["price"].pct_change()

    # Drop first row (NaN return)
    df.dropna(inplace=True)

    # Save to silver layer
    output_path = os.path.join(SILVER_PATH, "bitcoin_prices_clean.csv")
    df.to_csv(output_path)

    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data()
