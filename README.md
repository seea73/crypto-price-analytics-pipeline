# 💰 Cryptocurrency Price Analytics & Prediction Pipeline (Python)

An end-to-end cryptocurrency price analytics and machine learning pipeline built using Python.  
This project demonstrates real-world **data engineering**, **time-series analysis**, and **machine learning** practices using publicly available market data.

---

## 📌 Project Overview

Cryptocurrency markets are highly volatile and non-linear, making price analysis and prediction a challenging task.  
This project implements a complete pipeline that:

- Ingests real cryptocurrency price data via API  
- Cleans and preprocesses time-series data  
- Performs exploratory data analysis (EDA)  
- Engineers financial and temporal features  
- Trains and evaluates machine learning models  
- Follows a modern **Bronze–Silver–Gold** data pipeline architecture  

The project is designed to be **reproducible**, **modular**, and **research-ready**.

---

## 🧱 Repository Structure

```

crypto-price-analytics-pipeline/
├── data/
│ ├── bronze/ # Raw API data
│ ├── silver/ # Cleaned & preprocessed data
│ └── gold/ # Feature-engineered data
├── outputs/
│ ├── plots/ # EDA visualizations
│ └── model_results/ # Model predictions & metrics
├── paper/
│ ├── ieee_crypto_pipeline.pdf # IEEE camera-ready research paper
├── src/
│ ├── api_fetch.py
│ ├── preprocessing.py
│ ├── eda.py
│ ├── feature_engineering.py
│ └── model.py
├── requirements.txt
├── .gitignore
└── README.md

```
---

## 🧠 Pipeline Architecture

### 🟫 Bronze Layer — Raw Data Ingestion
- Fetches historical Bitcoin price data from a public cryptocurrency API  
- Stores raw, unmodified time-series data  

### 🟪 Silver Layer — Data Cleaning & Preprocessing
- Timestamp normalization  
- Missing value handling  
- Duplicate removal  
- Return calculation  

### 🟨 Gold Layer — Feature Engineering
- Lag-based price features  
- Simple and exponential moving averages (SMA, EMA)  
- Rolling volatility indicators  
- Model-ready dataset  

---

## 📊 Exploratory Data Analysis (EDA)

EDA is performed to analyze:

- Price trends over time  
- Return distributions  
- Market volatility  

Generated plots are saved in: 
ouputs/plots/

---

## 📈 Machine Learning Models

The following models are implemented:

- **Linear Regression** (baseline model)  
- **Random Forest Regressor** (non-linear ensemble model)  

### 📐 Evaluation Metrics
- Root Mean Squared Error (RMSE)  
- Mean Absolute Error (MAE)  
- R² Score  

Model outputs and prediction plots are stored in:
outputs/model_results/

---

## 🧪 Results Summary

| Model | RMSE (USD) | R² |
|------|------------|----|
| Linear Regression | 18.66 | 0.9999 |
| Random Forest | 117.56 | 0.9963 |

### 🔍 Key Insights
- Feature engineering significantly improves predictive performance  
- Lag-based and trend-oriented features capture strong temporal dependencies  
- High volatility limits perfect predictability in cryptocurrency markets  

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash ```
pip install -r requirements.txt

### 2️⃣ Run the Pipeline (in order)
-python src/api_fetch.py
-python src/preprocessing.py
-python src/eda.py
-python src/feature_engineering.py
-python src/model.py


## 🔁 Reproducibility & Data Ethics

- Data is sourced from publicly available cryptocurrency market APIs  
- No personal or sensitive data is used  
- The entire pipeline is fully reproducible using the provided scripts  
- Data and results can be regenerated at any time via API ingestion  

---

## 📄 Research Paper

This repository includes an IEEE-style research paper describing:

- Pipeline architecture  
- Mathematical formulation  
- Experimental evaluation  
- AI use disclosure and ethics  

See the `paper/` directory for:

- Camera-ready PDF  

---

## 🔮 Future Enhancements

- Multi-cryptocurrency prediction  
- Deep learning models (LSTM, GRU)  
- Real-time streaming pipelines  
- Dashboard interface (e.g., Streamlit)  
- Hyperparameter tuning  

---

## 👤 Author

**Sheena Patel**  
Independent Researcher

