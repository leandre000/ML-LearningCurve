"""
Example: Frequency Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from FrequencyEncoding import frequency_encode
import pandas as pd

# Sample data
data = {
    "product": ["A", "B", "C", "A", "B", "A", "C", "C"],
    "price": [10, 20, 30, 10, 20, 10, 30, 30]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nApplying frequency encoding to 'product' column:")
df['product_freq'] = frequency_encode(df['product'])
print(df[['product', 'product_freq']])

