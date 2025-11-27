"""
Helmert Encoding Implementation

Helmert encoding compares each level of a factor to the mean of subsequent levels.
Useful for ordered categorical variables.
"""

import pandas as pd
import numpy as np


def helmert_encode(series, categories=None):
    """
    Apply Helmert encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        categories: ordered list of categories (auto-determined if None)
        
    Returns:
        pandas DataFrame with Helmert encoded columns
    """
    if categories is None:
        categories = sorted(series.unique())
    
    n_categories = len(categories)
    n_contrasts = n_categories - 1
    
    # Create Helmert contrast matrix
    contrast_matrix = np.zeros((n_categories, n_contrasts))
    for i in range(n_contrasts):
        contrast_matrix[:i+1, i] = -1 / (i + 1)
        contrast_matrix[i+1:, i] = 1 / (n_categories - i - 1)
    
    # Map categories to indices
    category_to_idx = {cat: idx for idx, cat in enumerate(categories)}
    indices = series.map(category_to_idx)
    
    # Apply encoding
    encoded_data = contrast_matrix[indices.values]
    
    columns = [f'{series.name}_helmert_{i}' for i in range(n_contrasts)]
    return pd.DataFrame(encoded_data, columns=columns, index=series.index)


# Example usage
if __name__ == "__main__":
    data = {"size": ["small", "medium", "large", "small", "large"]}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    categories = ["small", "medium", "large"]
    encoded_df = helmert_encode(df['size'], categories=categories)
    
    print("\nHelmert Encoded DataFrame:")
    print(encoded_df)

