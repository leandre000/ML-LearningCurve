"""
Frequency Encoding Implementation

Frequency encoding replaces categorical values with their frequency in the dataset.
This technique helps preserve information about value distribution.

Author: ML Learning Curve Contributors
License: MIT
"""

import pandas as pd
import warnings


def frequency_encode(series, normalize=True):
    """
    Encode categorical values using their frequency in the dataset.
    
    Args:
        series: pandas Series with categorical data
        normalize: if True, returns normalized frequencies (probabilities),
                   if False, returns absolute counts
        
    Returns:
        pandas Series with frequency-encoded values
        
    Example:
        >>> import pandas as pd
        >>> data = pd.Series(["A", "B", "A", "B", "C"])
        >>> encoded = frequency_encode(data)
        >>> print(encoded)
    """
    if not isinstance(series, pd.Series):
        warnings.warn("Input should be a pandas Series. Converting...")
        series = pd.Series(series)
    
    if normalize:
        freq = series.value_counts(normalize=True)
    else:
        freq = series.value_counts()
    
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