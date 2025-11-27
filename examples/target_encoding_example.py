"""
Example: Target Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.target_encoding import target_encode
import pandas as pd

data = {
    "city": ["NYC", "LA", "Chicago", "NYC", "LA", "Chicago"],
    "price": [100, 150, 120, 110, 160, 125]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nTarget Encoded DataFrame:")
df['city_target'] = target_encode(df['city'], df['price'], smoothing=1.0)
print(df)

