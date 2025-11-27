"""
Frequency Encoding Implementation

Frequency encoding replaces categorical values with their frequency in the dataset.
This technique helps preserve information about value distribution.
"""

import pandas as pd


def frequency_encode(series):
    """
    Encode categorical values using their frequency in the dataset.
    
    Args:
        series: pandas Series with categorical data
        
    Returns:
        pandas Series with frequency-encoded values
    """
    freq = series.value_counts(normalize=True)
    return series.map(freq)


# Example usage
if __name__ == "__main__":
    data = {"color": ["red", "green", "blue", "red", "green"]}
    df = pd.DataFrame(data)
    
    # Apply frequency encoding
    df['color_freq'] = frequency_encode(df['color'])
    df = df.drop('color', axis=1)
    
    print("Frequency Encoded DataFrame:")
    print(df)