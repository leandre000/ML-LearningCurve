"""
Complete Pipeline Example: Data Preprocessing with Multiple Encodings
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from FrequencyEncoding import frequency_encode
from labelEncoding import label_encode
from one_hot_encoding import one_hot_encode
from utils.preprocessing import handle_missing_values
from utils.validation import check_missing_values

# Sample dataset
data = {
    "product": ["A", "B", "C", "A", "B", None, "C"],
    "size": ["small", "medium", "large", "small", "medium", "large", "small"],
    "color": ["red", "green", "blue", "red", "green", "blue", "red"],
    "price": [10, 20, 30, 15, 25, 35, 12]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nMissing values:")
print(check_missing_values(df))

# Handle missing values
df_clean = handle_missing_values(df, strategy='mode')
print("\nAfter handling missing values:")
print(df_clean)

# Apply different encodings
print("\n" + "="*60)
print("Applying Encodings:")
print("="*60)

# Frequency encoding
df_clean['product_freq'] = frequency_encode(df_clean['product'])
print("\nFrequency encoding applied to 'product'")

# Label encoding
df_clean['size_label'] = label_encode(df_clean['size'].tolist())
print("Label encoding applied to 'size'")

# One-hot encoding
df_encoded = one_hot_encode(df_clean, columns=["color"], drop_first=False)
print("One-hot encoding applied to 'color'")

print("\nFinal Encoded DataFrame:")
print(df_encoded)

