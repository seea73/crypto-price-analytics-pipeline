import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
DATA_PATH = "data/silver/bitcoin_prices_clean.csv"
PLOT_PATH = "outputs/plots"
os.makedirs(PLOT_PATH, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"], index_col="timestamp")

# =========================
# 1. Price Trend
# =========================
plt.figure(figsize=(12,5))
plt.plot(df.index, df["price"])
plt.title("Bitcoin Price Trend")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.savefig(f"{PLOT_PATH}/price_trend.png", dpi=300, bbox_inches="tight")
plt.show()

# =========================
# 2. Returns Over Time
# =========================
plt.figure(figsize=(12,5))
plt.plot(df.index, df["return"])
plt.title("Bitcoin Returns Over Time")
plt.xlabel("Date")
plt.ylabel("Return")
plt.grid(True)
plt.savefig(f"{PLOT_PATH}/returns_over_time.png", dpi=300, bbox_inches="tight")
plt.show()

# =========================
# 3. Returns Distribution
# =========================
plt.figure(figsize=(8,5))
sns.histplot(df["return"], bins=50, kde=True)
plt.title("Distribution of Bitcoin Returns")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.savefig(f"{PLOT_PATH}/returns_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

# =========================
# 4. Rolling Volatility
# =========================
df["volatility_7d"] = df["return"].rolling(window=7).std()

plt.figure(figsize=(12,5))
plt.plot(df.index, df["volatility_7d"])
plt.title("7-Day Rolling Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.grid(True)
plt.savefig(f"{PLOT_PATH}/rolling_volatility.png", dpi=300, bbox_inches="tight")
plt.show()
