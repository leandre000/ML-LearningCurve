"""
Binary Encoding Implementation

Binary encoding is a combination of hash encoding and one-hot encoding.
It reduces dimensionality compared to one-hot encoding.
"""

import pandas as pd
import numpy as np


def binary_encode(series, n_bits=None):
    """
    Apply binary encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        n_bits: number of bits to use (auto-calculated if None)
        
    Returns:
        pandas DataFrame with binary encoded columns
    """
    unique_values = series.unique()
    n_unique = len(unique_values)
    
    if n_bits is None:
        n_bits = int(np.ceil(np.log2(n_unique)))
    
    # Create mapping
    mapping = {val: idx for idx, val in enumerate(unique_values)}
    
    # Convert to binary
    encoded_data = []
    for val in series:
        idx = mapping[val]
        binary = format(idx, f'0{n_bits}b')
        encoded_data.append([int(bit) for bit in binary])
    
    # Create DataFrame
    columns = [f'{series.name}_bin_{i}' for i in range(n_bits)]
    return pd.DataFrame(encoded_data, columns=columns, index=series.index)


# Example usage
if __name__ == "__main__":
    data = {"category": ["A", "B", "C", "D", "A", "B"]}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    encoded_df = binary_encode(df['category'])
    
    print("\nBinary Encoded DataFrame:")
    print(encoded_df)

