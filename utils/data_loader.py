"""
Data Loading Utilities
"""

import pandas as pd
import os


def load_csv(filepath, **kwargs):
    """
    Load data from CSV file.
    
    Args:
        filepath: path to CSV file
        **kwargs: additional arguments to pass to pd.read_csv
        
    Returns:
        pandas DataFrame
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(filepath, **kwargs)


def load_excel(filepath, sheet_name=0):
    """
    Load data from Excel file.
    
    Args:
        filepath: path to Excel file
        sheet_name: sheet name or index
        
    Returns:
        pandas DataFrame
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_excel(filepath, sheet_name=sheet_name)

