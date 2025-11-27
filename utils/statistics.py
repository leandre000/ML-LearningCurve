"""
Statistical Utilities
"""

import pandas as pd
import numpy as np


def calculate_cardinality(df, columns=None):
    """
    Calculate cardinality (number of unique values) for columns.
    
    Args:
        df: pandas DataFrame
        columns: list of column names (all columns if None)
        
    Returns:
        Series with cardinality for each column
    """
    if columns is None:
        columns = df.columns
    
    return df[columns].nunique()


def calculate_entropy(series):
    """
    Calculate entropy of a categorical series.
    
    Args:
        series: pandas Series with categorical data
        
    Returns:
        float: entropy value
    """
    value_counts = series.value_counts(normalize=True)
    return -np.sum(value_counts * np.log2(value_counts + 1e-10))

