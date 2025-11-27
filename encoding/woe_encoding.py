"""
Weight of Evidence (WoE) Encoding Implementation

WoE encoding is commonly used in credit scoring and binary classification.
It measures the strength of the relationship between a feature and target.
"""

import pandas as pd
import numpy as np


def woe_encode(series, target, epsilon=1e-10):
    """
    Apply Weight of Evidence encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        target: pandas Series with binary target (0/1)
        epsilon: small value to avoid division by zero
        
    Returns:
        pandas Series with WoE-encoded values
    """
    # Calculate distributions
    df_temp = pd.DataFrame({'feature': series, 'target': target})
    
    # Group by feature and calculate WoE
    grouped = df_temp.groupby('feature')['target'].agg(['sum', 'count'])
    grouped['non_events'] = grouped['count'] - grouped['sum']
    
    # Calculate overall distributions
    total_events = target.sum()
    total_non_events = len(target) - total_events
    
    # Calculate WoE
    grouped['woe'] = np.log(
        (grouped['sum'] / total_events + epsilon) / 
        (grouped['non_events'] / total_non_events + epsilon)
    )
    
    return series.map(grouped['woe']).fillna(0)


# Example usage
if __name__ == "__main__":
    data = {
        "category": ["A", "B", "A", "B", "C", "A", "C"],
        "target": [1, 0, 1, 0, 1, 1, 0]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    df['category_woe'] = woe_encode(df['category'], df['target'])
    
    print("\nWoE Encoded DataFrame:")
    print(df)

