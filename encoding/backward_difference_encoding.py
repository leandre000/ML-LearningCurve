"""
Backward Difference Encoding Implementation

Backward difference encoding compares each level of a factor to the previous level.
Useful for ordered categorical variables in regression models.
"""

import pandas as pd
import numpy as np


def backward_difference_encode(series, categories=None):
    """
    Apply backward difference encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        categories: ordered list of categories (auto-determined if None)
        
    Returns:
        pandas DataFrame with backward difference encoded columns
    """
    if categories is None:
        categories = sorted(series.unique())
    
    n_categories = len(categories)
    n_contrasts = n_categories - 1
    
    # Create contrast matrix
    contrast_matrix = np.zeros((n_categories, n_contrasts))
    for i in range(n_contrasts):
        contrast_matrix[:i+1, i] = -1 / (i + 1)
        contrast_matrix[i+1, i] = 1
    
    # Map categories to indices
    category_to_idx = {cat: idx for idx, cat in enumerate(categories)}
    indices = series.map(category_to_idx)
    
    # Apply encoding
    encoded_data = contrast_matrix[indices.values]
    
    columns = [f'{series.name}_bd_{i}' for i in range(n_contrasts)]
    return pd.DataFrame(encoded_data, columns=columns, index=series.index)


# Example usage
if __name__ == "__main__":
    data = {"education": ["high_school", "bachelor", "master", "phd", "bachelor"]}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    categories = ["high_school", "bachelor", "master", "phd"]
    encoded_df = backward_difference_encode(df['education'], categories=categories)
    
    print("\nBackward Difference Encoded DataFrame:")
    print(encoded_df)

