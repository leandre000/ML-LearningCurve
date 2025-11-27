"""
Example: Helmert Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.helmert_encoding import helmert_encode
import pandas as pd

data = {
    "education": ["high_school", "bachelor", "master", "phd", "bachelor"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

categories = ["high_school", "bachelor", "master", "phd"]
encoded_df = helmert_encode(df['education'], categories=categories)

print("\nHelmert Encoded DataFrame:")
print(encoded_df)

