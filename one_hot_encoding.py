"""
One-Hot Encoding Implementation

One-hot encoding creates binary columns for each category.
Each category gets its own column with 1 or 0 values.
"""

import pandas as pd


def one_hot_encode(df, columns):
    """
    Apply one-hot encoding to specified columns.
    
    Args:
        df: pandas DataFrame
        columns: list of column names to encode
        
    Returns:
        pandas DataFrame with one-hot encoded columns
    """
    return pd.get_dummies(df, columns=columns)


# Example usage
if __name__ == "__main__":
    data = {"color": ["yellow", "red", "green"]}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    one_hot_encoded_df = one_hot_encode(df, columns=["color"])
    
    print("\nOne-Hot Encoded DataFrame:")
    print(one_hot_encoded_df)
