# Futures Data Pipeline 🚀

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![License](https://img.shields.io/badge/License-MIT-orange)

**Core data preprocessing engine for [DeepAlpha Terminal](https://www.trading-brains.com).**

This repository contains the standardized ETL (Extract, Transform, Load) scripts used by **Trading Brains Studio** to process high-frequency futures data from Chinese exchanges (SHFE, DCE, CZCE).

## Features

- ⚡ **High Performance**: Optimized for processing large CSV tick data using Pandas vectorization.
- 🧹 **Smart Cleaning**: Auto-detection of bad ticks and outliers in OHLC streams.
- 🔄 **Format Conversion**: Converts raw exchange CSVs into TqSdk-compatible formats (HDF5/Parquet).
- 🛡️ **Reliability**: robust missing value handling for continuous contract construction.

## Usage

```python
from cleaner import FuturesDataCleaner

# Initialize pipeline
pipeline = FuturesDataCleaner("data/raw/rb_main.csv")

# Execute cleaning steps
pipeline.load_data()
pipeline.remove_outliers(threshold=0.05)
pipeline.export_processed_data("data/clean/rb_main.h5")

Integration
This module is integrated into the backend of DeepAlpha Pro.
© 2026 Trading Brains Studio.
