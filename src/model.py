import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Paths
DATA_PATH = "data/gold/bitcoin_features.csv"
OUTPUT_PATH = "outputs/model_results"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def train_models():
    # Load gold data
    df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"], index_col="timestamp")

    # =========================
    # Feature / Target Split
    # =========================
    X = df.drop(columns=["price"])
    y = df["price"]

    # =========================
    # Time-Series Split (NO SHUFFLE)
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # =========================
    # Models
    # =========================
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(
            n_estimators=100, random_state=42
        )
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        rmse = np.sqrt(mean_squared_error(y_test, preds))
        mae = mean_absolute_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        results[name] = {
            "RMSE": rmse,
            "MAE": mae,
            "R2": r2
        }

        # =========================
        # Prediction Plot
        # =========================
        plt.figure(figsize=(12,5))
        plt.plot(y_test.index, y_test, label="Actual Price")
        plt.plot(y_test.index, preds, label="Predicted Price")
        plt.title(f"{name} – Actual vs Predicted BTC Price")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{OUTPUT_PATH}/{name.replace(' ', '_')}_prediction.png",
                    dpi=300, bbox_inches="tight")
        plt.show()

    # Save metrics
    results_df = pd.DataFrame(results).T
    results_df.to_csv(f"{OUTPUT_PATH}/model_metrics.csv")

    print("✅ Model training completed")
    print(results_df)

if __name__ == "__main__":
    train_models()
