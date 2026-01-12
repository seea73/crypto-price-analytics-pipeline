import pandas as pd
import os

# Paths
SILVER_PATH = "data/silver/bitcoin_prices_clean.csv"
GOLD_PATH = "data/gold"
os.makedirs(GOLD_PATH, exist_ok=True)

def create_features():
    # Load cleaned data
    df = pd.read_csv(SILVER_PATH, parse_dates=["timestamp"], index_col="timestamp")

    # =========================
    # Lag Features
    # =========================
    df["price_lag_1"] = df["price"].shift(1)
    df["price_lag_2"] = df["price"].shift(2)
    df["price_lag_3"] = df["price"].shift(3)

    # =========================
    # Moving Averages
    # =========================
    df["sma_5"] = df["price"].rolling(window=5).mean()
    df["sma_10"] = df["price"].rolling(window=10).mean()

    df["ema_5"] = df["price"].ewm(span=5, adjust=False).mean()
    df["ema_10"] = df["price"].ewm(span=10, adjust=False).mean()

    # =========================
    # Rolling Volatility
    # =========================
    df["volatility_7"] = df["return"].rolling(window=7).std()
    df["volatility_14"] = df["return"].rolling(window=14).std()

    # Drop rows with NaNs caused by rolling calculations
    df.dropna(inplace=True)

    # Save gold data
    output_path = os.path.join(GOLD_PATH, "bitcoin_features.csv")
    df.to_csv(output_path)

    print(f"✅ Gold layer data saved to {output_path}")

if __name__ == "__main__":
    create_features()
