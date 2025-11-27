"""
Visualization Utilities
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_encoding_comparison(original, encoded_dict, title="Encoding Comparison"):
    """
    Plot comparison of different encodings.
    
    Args:
        original: original categorical data
        encoded_dict: dictionary of {encoding_name: encoded_data}
        title: plot title
    """
    fig, axes = plt.subplots(1, len(encoded_dict) + 1, figsize=(15, 5))
    
    # Plot original
    original.value_counts().plot(kind='bar', ax=axes[0], title='Original')
    
    # Plot encodings
    for idx, (name, encoded) in enumerate(encoded_dict.items(), 1):
        if isinstance(encoded, pd.Series):
            encoded.plot(kind='hist', ax=axes[idx], title=name)
        elif isinstance(encoded, pd.DataFrame):
            encoded.sum().plot(kind='bar', ax=axes[idx], title=name)
    
    plt.suptitle(title)
    plt.tight_layout()
    return fig

