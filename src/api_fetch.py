import requests
import pandas as pd
from datetime import datetime
import os

# Create bronze directory if not exists
BRONZE_PATH = "data/bronze"
os.makedirs(BRONZE_PATH, exist_ok=True)

def fetch_crypto_data(coin_id="bitcoin", vs_currency="usd", days=90):
    """
    Fetch historical crypto price data from CoinGecko API
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    
    params = {
        "vs_currency": vs_currency,
        "days": days
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return data

def save_raw_data(data, coin_id="bitcoin"):
    """
    Save raw price data to Bronze layer
    """
    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    prices["timestamp"] = pd.to_datetime(prices["timestamp"], unit="ms")

    file_name = f"{coin_id}_prices_raw.csv"
    file_path = os.path.join(BRONZE_PATH, file_name)
    
    prices.to_csv(file_path, index=False)
    print(f"✅ Raw data saved to {file_path}")

if __name__ == "__main__":
    raw_data = fetch_crypto_data()
    save_raw_data(raw_data)
