"""
One-Hot Encoding Implementation

One-hot encoding creates binary columns for each category.
Each category gets its own column with 1 or 0 values.

Author: ML Learning Curve Contributors
License: MIT
"""

import pandas as pd
import warnings


def one_hot_encode(df, columns, drop_first=False, dtype=int):
    """
    Apply one-hot encoding to specified columns.
    
    Args:
        df: pandas DataFrame
        columns: list of column names to encode, or single column name
        drop_first: if True, drops first category to avoid multicollinearity
        dtype: data type for encoded columns (default: int)
        
    Returns:
        pandas DataFrame with one-hot encoded columns
        
    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({"color": ["red", "green", "blue"]})
        >>> encoded = one_hot_encode(df, columns=["color"])
        >>> print(encoded)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    if isinstance(columns, str):
        columns = [columns]
    
    for col in columns:
        if col not in df.columns:
            warnings.warn(f"Column '{col}' not found in DataFrame")
    
    return pd.get_dummies(df, columns=columns, drop_first=drop_first, dtype=dtype)


# Example usage
if __name__ == "__main__":
    data = {"color": ["yellow", "red", "green"]}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    one_hot_encoded_df = one_hot_encode(df, columns=["color"])
    
    print("\nOne-Hot Encoded DataFrame:")
    print(one_hot_encoded_df)
