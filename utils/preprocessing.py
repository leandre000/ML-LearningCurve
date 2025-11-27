"""
Data Preprocessing Utilities
"""

import pandas as pd
import numpy as np


def handle_missing_values(df, strategy='mean'):
    """
    Handle missing values in DataFrame.
    
    Args:
        df: pandas DataFrame
        strategy: 'mean', 'median', 'mode', or 'drop'
        
    Returns:
        pandas DataFrame with handled missing values
    """
    df_clean = df.copy()
    
    for col in df_clean.columns:
        if df_clean[col].isnull().any():
            if strategy == 'mean' and df_clean[col].dtype in ['int64', 'float64']:
                df_clean[col].fillna(df_clean[col].mean(), inplace=True)
            elif strategy == 'median' and df_clean[col].dtype in ['int64', 'float64']:
                df_clean[col].fillna(df_clean[col].median(), inplace=True)
            elif strategy == 'mode':
                df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
            elif strategy == 'drop':
                df_clean.dropna(subset=[col], inplace=True)
    
    return df_clean

