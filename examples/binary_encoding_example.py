"""
Example: Binary Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.binary_encoding import binary_encode
import pandas as pd

data = {"category": ["A", "B", "C", "D", "E", "F"]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nBinary Encoded DataFrame:")
encoded_df = binary_encode(df['category'])
print(encoded_df)

