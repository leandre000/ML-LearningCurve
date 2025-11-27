"""
Data Validation Utilities
"""

import pandas as pd
import numpy as np


def check_missing_values(df):
    """
    Check for missing values in DataFrame.
    
    Args:
        df: pandas DataFrame
        
    Returns:
        Series with missing value counts
    """
    return df.isnull().sum()

