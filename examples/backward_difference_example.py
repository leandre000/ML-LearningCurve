"""
Example: Backward Difference Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.backward_difference_encoding import backward_difference_encode
import pandas as pd

data = {
    "size": ["small", "medium", "large", "small", "large"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

categories = ["small", "medium", "large"]
encoded_df = backward_difference_encode(df['size'], categories=categories)

print("\nBackward Difference Encoded DataFrame:")
print(encoded_df)

