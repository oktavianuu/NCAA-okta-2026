# data_loader.py
import pandas as pd
from pathlib import Path

def load_data(file_path, **kwargs):
    """Load data from CSV, Excel, JSON, Parquet based on extension."""
    file_path = Path(file_path)
    ext = file_path.suffix.lower()
    
    readers = {
        '.csv': pd.read_csv,
        '.xls': pd.read_excel,
        '.xlsx': pd.read_excel,
        '.json': pd.read_json,
        '.parquet': pd.read_parquet,
    }
    if ext not in readers:
        raise ValueError(f"Unsupported file type: {ext}")
    return readers[ext](file_path, **kwargs)