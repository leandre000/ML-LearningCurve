"""
Example: One-Hot Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from one_hot_encoding import one_hot_encode
import pandas as pd

# Sample data
data = {
    "city": ["NYC", "LA", "Chicago", "NYC"],
    "temperature": [72, 75, 68, 70]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nOne-Hot Encoded DataFrame:")
encoded_df = one_hot_encode(df, columns=["city"])
print(encoded_df)

