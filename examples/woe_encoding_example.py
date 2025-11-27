"""
Example: Weight of Evidence Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.woe_encoding import woe_encode
import pandas as pd

data = {
    "credit_score": ["high", "medium", "low", "high", "medium", "low"],
    "default": [0, 1, 1, 0, 0, 1]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nWoE Encoded DataFrame:")
df['credit_score_woe'] = woe_encode(df['credit_score'], df['default'])
print(df)

