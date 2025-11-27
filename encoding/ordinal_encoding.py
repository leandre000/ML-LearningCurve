"""
Ordinal Encoding Implementation

Ordinal encoding assigns integer values to categories based on a specified order.
Useful when categories have a natural ordering.
"""

import pandas as pd


def ordinal_encode(series, categories=None):
    """
    Apply ordinal encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        categories: ordered list of categories (auto-determined if None)
        
    Returns:
        pandas Series with ordinal-encoded values
    """
    if categories is None:
        categories = sorted(series.unique())
    
    mapping = {cat: idx for idx, cat in enumerate(categories)}
    return series.map(mapping)


# Example usage
if __name__ == "__main__":
    data = {"size": ["small", "medium", "large", "small", "large"]}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    df['size_ordinal'] = ordinal_encode(df['size'], categories=["small", "medium", "large"])
    
    print("\nOrdinal Encoded DataFrame:")
    print(df)

