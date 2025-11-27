"""
Example: Leave-One-Out Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.leave_one_out_encoding import leave_one_out_encode
import pandas as pd

data = {
    "product": ["A", "B", "A", "B", "C", "A"],
    "sales": [100, 200, 150, 250, 300, 120]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nLeave-One-Out Encoded DataFrame:")
df['product_loo'] = leave_one_out_encode(df['product'], df['sales'])
print(df)

