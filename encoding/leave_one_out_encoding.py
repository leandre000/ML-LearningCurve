"""
Leave-One-Out Encoding Implementation

Leave-one-out encoding is a variant of target encoding that excludes
the current row when calculating the mean, reducing overfitting.
"""

import pandas as pd
import numpy as np


def leave_one_out_encode(series, target):
    """
    Apply leave-one-out encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        target: pandas Series with target values
        
    Returns:
        pandas Series with leave-one-out encoded values
    """
    df_temp = pd.DataFrame({'feature': series, 'target': target})
    df_temp['index'] = df_temp.index
    
    def calculate_loo_mean(row):
        category = row['feature']
        current_idx = row['index']
        # Calculate mean excluding current row
        mask = (df_temp['feature'] == category) & (df_temp['index'] != current_idx)
        if mask.sum() > 0:
            return df_temp.loc[mask, 'target'].mean()
        else:
            return target.mean()
    
    return df_temp.apply(calculate_loo_mean, axis=1)


# Example usage
if __name__ == "__main__":
    data = {
        "category": ["A", "B", "A", "B", "C", "A"],
        "target": [10, 20, 15, 25, 30, 12]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    df['category_loo'] = leave_one_out_encode(df['category'], df['target'])
    
    print("\nLeave-One-Out Encoded DataFrame:")
    print(df)

