"""
Encoding Comparison Utilities
"""

import pandas as pd
import numpy as np


def compare_encodings(df, column):
    """
    Compare different encoding techniques on a column.
    
    Args:
        df: pandas DataFrame
        column: column name to encode
        
    Returns:
        dict: comparison results
    """
    results = {}
    
    # Frequency encoding
    freq = df[column].value_counts(normalize=True)
    results['frequency'] = df[column].map(freq)
    
    return results

