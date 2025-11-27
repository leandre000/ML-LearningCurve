"""
Label Encoding Implementation

Label encoding converts categorical text data into numerical format.
Each unique category is assigned a unique integer.
"""

from sklearn.preprocessing import LabelEncoder


def label_encode(data):
    """
    Encode categorical data using label encoding.
    
    Args:
        data: list or array-like of categorical values
        
    Returns:
        tuple: (encoded_data, label_encoder) - encoded values and encoder object
    """
    label_encoder = LabelEncoder()
    encoded_data = label_encoder.fit_transform(data)
    return encoded_data, label_encoder


# Example usage
if __name__ == "__main__":
    data = ["small", "medium", "large", "small", "large"]
    
    encoded_data, encoder = label_encode(data)
    
    print("Original data:", data)
    print("Encoded data:", encoded_data)
    print("Classes:", encoder.classes_)