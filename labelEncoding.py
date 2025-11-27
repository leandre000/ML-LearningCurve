"""
Label Encoding Implementation

Label encoding converts categorical text data into numerical format.
Each unique category is assigned a unique integer.

Author: ML Learning Curve Contributors
License: MIT
"""

from sklearn.preprocessing import LabelEncoder
import numpy as np
import warnings


def label_encode(data, return_encoder=False):
    """
    Encode categorical data using label encoding.
    
    Args:
        data: list, array, or pandas Series of categorical values
        return_encoder: if True, returns encoder object along with encoded data
        
    Returns:
        if return_encoder=False: numpy array with encoded values
        if return_encoder=True: tuple (encoded_data, label_encoder)
        
    Example:
        >>> data = ["small", "medium", "large"]
        >>> encoded = label_encode(data)
        >>> print(encoded)
    """
    if not isinstance(data, (list, np.ndarray)):
        try:
            data = data.tolist()
        except AttributeError:
            warnings.warn("Converting input to list")
            data = list(data)
    
    label_encoder = LabelEncoder()
    encoded_data = label_encoder.fit_transform(data)
    
    if return_encoder:
        return encoded_data, label_encoder
    return encoded_data


# Example usage
if __name__ == "__main__":
    data = ["small", "medium", "large", "small", "large"]
    
    encoded_data, encoder = label_encode(data)
    
    print("Original data:", data)
    print("Encoded data:", encoded_data)
    print("Classes:", encoder.classes_)