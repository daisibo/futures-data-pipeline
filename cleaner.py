import pandas as pd
import numpy as np
from typing import Optional
from datetime import datetime

class FuturesDataCleaner:
    """
    Standardized data cleaning pipeline for Futures Tick/Bar data.
    Used by Trading Brains Studio for historical data preprocessing.
    """
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df: Optional[pd.DataFrame] = None

    def load_data(self) -> None:
        """Load raw CSV data with optimized types."""
        try:
            self.df = pd.read_csv(self.filepath)
            print(f"[INFO] Successfully loaded {self.filepath}")
        except Exception as e:
            print(f"[ERROR] Failed to load data: {e}")

    def clean_timestamps(self, time_col: str = 'datetime') -> None:
        """Convert timestamps and set index."""
        if self.df is not None:
            self.df[time_col] = pd.to_datetime(self.df[time_col])
            self.df.set_index(time_col, inplace=True)
            self.df.sort_index(inplace=True)

    def fill_missing_values(self) -> None:
        """Forward fill specifically for financial time-series."""
        if self.df is not None:
            # Forward fill price data (logical for markets)
            cols = ['Open', 'High', 'Low', 'Close']
            self.df[cols] = self.df[cols].ffill()
            # Fill volume with 0
            self.df['Volume'] = self.df['Volume'].fillna(0)

    def remove_outliers(self, threshold: float = 0.1) -> None:
        """
        Simple outlier detection based on percentage change.
        Removes ticks that deviate significantly from previous tick.
        """
        if self.df is not None:
            pct_change = self.df['Close'].pct_change().abs()
            self.df = self.df[pct_change < threshold]

    def export_processed_data(self, output_path: str) -> None:
        """Save to HDF5 for high-speed access in TqSdk."""
        if self.df is not None:
            self.df.to_hdf(output_path, key='data', mode='w')
            print(f"[SUCCESS] Data saved to {output_path}")

if __name__ == "__main__":
    # Example usage for Trading Brains Studio workflow
    cleaner = FuturesDataCleaner("./raw_data/rb2605.csv")
    cleaner.load_data()
    cleaner.clean_timestamps()
    cleaner.fill_missing_values()
    cleaner.export_processed_data("./processed/rb2605.h5")
