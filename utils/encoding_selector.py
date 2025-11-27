"""
Encoding Technique Selector

Automatically selects the best encoding technique based on data characteristics.
"""

import pandas as pd
import numpy as np
from utils.statistics import calculate_cardinality, calculate_entropy


def select_encoding(series, target=None, is_ordinal=False, max_cardinality=100):
    """
    Select the best encoding technique based on data characteristics.
    
    Args:
        series: pandas Series with categorical data
        target: optional target variable for supervised encoding
        is_ordinal: whether the data is ordinal
        max_cardinality: maximum cardinality threshold
        
    Returns:
        str: recommended encoding technique name
    """
    cardinality = series.nunique()
    
    if is_ordinal:
        if cardinality <= 10:
            return "ordinal"
        else:
            return "label"
    
    if target is not None:
        if len(target.unique()) == 2:
            return "woe"  # Binary classification
        else:
            return "target"  # Multi-class or regression
    
    if cardinality < 10:
        return "one_hot"
    elif cardinality < max_cardinality:
        return "binary"
    else:
        return "hash"


def get_encoding_recommendations(df, categorical_columns=None):
    """
    Get encoding recommendations for all categorical columns.
    
    Args:
        df: pandas DataFrame
        categorical_columns: list of categorical column names (auto-detected if None)
        
    Returns:
        dict: mapping of column names to recommended encodings
    """
    if categorical_columns is None:
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    recommendations = {}
    for col in categorical_columns:
        cardinality = df[col].nunique()
        recommendations[col] = {
            'encoding': select_encoding(df[col]),
            'cardinality': cardinality,
            'entropy': calculate_entropy(df[col])
        }
    
    return recommendations

