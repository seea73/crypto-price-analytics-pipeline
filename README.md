# Cryptocurrency Price Analytics & Prediction Pipeline (Python)

An end-to-end cryptocurrency price analytics and machine learning pipeline built using Python. This project demonstrates real-world data engineering, time-series analysis, and machine learning practices using publicly available market data.

Project Overview
Cryptocurrency markets are highly volatile and non-linear, making price analysis and prediction a challenging task. This project implements a complete pipeline that ingests real cryptocurrency price data via API, cleans and preprocesses time-series data, performs exploratory data analysis (EDA), engineers financial and temporal features, trains and evaluates machine learning models, and follows a modern Bronze–Silver–Gold data pipeline architecture. The project is designed to be reproducible, modular, and research-ready.

Repository Structure
crypto-price-analytics-pipeline/
data/
  bronze/    Raw API data
  silver/    Cleaned and preprocessed data
  gold/      Feature-engineered data
outputs/
  plots/         EDA visualizations
  model_results/ Model predictions and metrics
paper/
  ieee_crypto_pipeline.pdf   IEEE camera-ready research paper
  ieee_crypto_pipeline.tex   LaTeX source
src/
  api_fetch.py
  preprocessing.py
  eda.py
  feature_engineering.py
  model.py
notebooks/
requirements.txt
.gitignore
README.md

Pipeline Architecture
Bronze Layer: Raw data ingestion from a public cryptocurrency API with no modification.
Silver Layer: Data cleaning and preprocessing including timestamp normalization, missing value handling, duplicate removal, and return calculation.
Gold Layer: Feature engineering including lag-based features, moving averages, rolling volatility, and model-ready datasets.

Exploratory Data Analysis (EDA)
EDA is performed to analyze price trends, return distributions, and market volatility. Generated plots are saved in the outputs/plots directory.

Machine Learning Models
The following models are implemented:
- Linear Regression (baseline model)
- Random Forest Regressor (non-linear ensemble model)

Evaluation Metrics
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score

Results Summary
Linear Regression achieved an RMSE of 18.66 USD with an R² score of 0.9999.
Random Forest achieved an RMSE of 117.56 USD with an R² score of 0.9963.

Key insights include improved predictive performance through feature engineering, strong temporal dependencies captured by lag-based features, and the impact of volatility on model accuracy.

How to Run the Project
Step 1: Install dependencies
pip install -r requirements.txt

Step 2: Run the pipeline in order
python src/api_fetch.py
python src/preprocessing.py
python src/eda.py
python src/feature_engineering.py
python src/model.py

Reproducibility and Data Ethics
All data used in this project is obtained from publicly available cryptocurrency market APIs. No personal or sensitive data is used. The entire pipeline is fully reproducible using the provided scripts, and all results can be regenerated via API ingestion.

Research Paper
This repository includes an IEEE-style research paper describing the pipeline architecture, mathematical formulation, experimental evaluation, and AI use disclosure. The paper is available in the paper directory in both PDF and LaTeX formats.

Future Enhancements
Planned improvements include multi-cryptocurrency prediction, deep learning models such as LSTM and GRU, real-time streaming pipelines, dashboard interfaces, and hyperparameter tuning.

Author
Sheena Patel
Independent Researcher

License
This project is intended for educational and research purposes.
