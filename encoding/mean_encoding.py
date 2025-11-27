"""
Mean Encoding Implementation

Mean encoding replaces categories with the mean of the target variable.
Similar to target encoding but without smoothing.
"""

import pandas as pd


def mean_encode(series, target):
    """
    Apply mean encoding to categorical data.
    
    Args:
        series: pandas Series with categorical data
        target: pandas Series with target values
        
    Returns:
        pandas Series with mean-encoded values
    """
    mean_target = target.groupby(series).mean()
    return series.map(mean_target).fillna(target.mean())


# Example usage
if __name__ == "__main__":
    data = {
        "category": ["A", "B", "A", "B", "C"],
        "target": [10, 20, 15, 25, 30]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    
    df['category_mean'] = mean_encode(df['category'], df['target'])
    
    print("\nMean Encoded DataFrame:")
    print(df)

