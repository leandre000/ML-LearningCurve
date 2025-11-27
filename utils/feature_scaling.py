"""
Feature Scaling Utilities
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def standard_scale(df, columns):
    """
    Apply standard scaling (z-score normalization) to columns.
    
    Args:
        df: pandas DataFrame
        columns: list of column names to scale
        
    Returns:
        tuple: (scaled_df, scaler)
    """
    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    return df_scaled, scaler


def minmax_scale(df, columns):
    """
    Apply min-max scaling to columns.
    
    Args:
        df: pandas DataFrame
        columns: list of column names to scale
        
    Returns:
        tuple: (scaled_df, scaler)
    """
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[columns] = scaler.fit_transform(df[columns])
    return df_scaled, scaler

