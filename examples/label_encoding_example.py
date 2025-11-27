"""
Example: Label Encoding Usage
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from labelEncoding import label_encode

# Sample data
sizes = ["small", "medium", "large", "small", "large", "medium"]

encoded, encoder = label_encode(sizes)

print("Original data:", sizes)
print("Encoded data:", encoded)
print("Class mapping:", dict(zip(encoder.classes_, range(len(encoder.classes_)))))

