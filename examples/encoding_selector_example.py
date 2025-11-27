"""
Example: Using the Encoding Selector
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.encoding_selector import get_encoding_recommendations
import pandas as pd

# Sample dataset with different categorical characteristics
data = {
    "low_cardinality": ["A", "B", "C", "A", "B"],
    "high_cardinality": [f"cat_{i}" for i in range(200)],
    "ordinal_size": ["small", "medium", "large", "small", "large"],
    "binary_target": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df.head())
print("\n" + "="*60)
print("Encoding Recommendations:")
print("="*60)

recommendations = get_encoding_recommendations(df, categorical_columns=["low_cardinality", "high_cardinality", "ordinal_size"])

for col, info in recommendations.items():
    print(f"\n{col}:")
    print(f"  Recommended: {info['encoding']}")
    print(f"  Cardinality: {info['cardinality']}")
    print(f"  Entropy: {info['entropy']:.4f}")

