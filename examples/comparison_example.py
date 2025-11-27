"""
Example: Comparing Different Encoding Techniques
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from FrequencyEncoding import frequency_encode
from labelEncoding import label_encode
from one_hot_encoding import one_hot_encode

# Sample data
data = {"category": ["A", "B", "C", "A", "B", "A"]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "="*50)

# Frequency Encoding
df_freq = df.copy()
df_freq['category_freq'] = frequency_encode(df_freq['category'])
print("\nFrequency Encoding:")
print(df_freq[['category', 'category_freq']])

# Label Encoding
encoded, encoder = label_encode(df['category'].tolist())
df_label = df.copy()
df_label['category_label'] = encoded
print("\nLabel Encoding:")
print(df_label[['category', 'category_label']])

# One-Hot Encoding
df_onehot = one_hot_encode(df, columns=["category"])
print("\nOne-Hot Encoding:")
print(df_onehot)

