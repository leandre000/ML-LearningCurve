"""
Target Encoding Implementation

Target encoding replaces categorical values with the mean of the target variable
for that category. Useful for supervised learning tasks.
"""

import pandas as pd
import numpy as np


def target_encode(series, target, smoothing=1.0):
    """
    Apply target encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        target: pandas Series with target values
        smoothing: smoothing factor to reduce overfitting
        
    Returns:
        pandas Series with target-encoded values
    """
    # Calculate mean target per category
    mean_target = target.groupby(series).mean()
    
    # Global mean
    global_mean = target.mean()
    
    # Count per category
    count = series.value_counts()
    
    # Apply smoothing
    encoded = series.map(mean_target)
    smoothing_factor = count / (count + smoothing)
    encoded = smoothing_factor * encoded + (1 - smoothing_factor) * global_mean
    
    return encoded.fillna(global_mean)


# Example usage
if __name__ == "__main__":
    data = {
        "category": ["A", "B", "A", "B", "C", "A", "C"],
        "target": [1, 0, 1, 0, 1, 1, 0]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    df['category_target_encoded'] = target_encode(df['category'], df['target'])
    
    print("\nTarget Encoded DataFrame:")
    print(df)

