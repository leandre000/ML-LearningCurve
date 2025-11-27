"""
Hash Encoding Implementation

Hash encoding uses a hash function to map categories to a fixed number of features.
Useful for high cardinality categorical features.
"""

import pandas as pd
import numpy as np


def hash_encode(series, n_features=10):
    """
    Apply hash encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        n_features: number of hash features to create
        
    Returns:
        pandas DataFrame with hash encoded columns
    """
    encoded_data = []
    
    for val in series:
        hash_val = hash(str(val))
        features = []
        for i in range(n_features):
            # Use different hash seeds for each feature
            feature_hash = hash(f"{val}_{i}")
            features.append(feature_hash % 2)  # Binary feature
        encoded_data.append(features)
    
    columns = [f'{series.name}_hash_{i}' for i in range(n_features)]
    return pd.DataFrame(encoded_data, columns=columns, index=series.index)


# Example usage
if __name__ == "__main__":
    data = {"category": ["A", "B", "C", "D", "E", "F"]}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    encoded_df = hash_encode(df['category'], n_features=5)
    
    print("\nHash Encoded DataFrame (5 features):")
    print(encoded_df)

