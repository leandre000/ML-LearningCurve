"""
Benchmark script to compare encoding techniques performance
"""

import sys
import os
import time
import pandas as pd
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from FrequencyEncoding import frequency_encode
from labelEncoding import label_encode
from one_hot_encoding import one_hot_encode
from encoding.binary_encoding import binary_encode

def benchmark_encoding(func, data, name):
    """Benchmark an encoding function"""
    start = time.time()
    result = func(data)
    end = time.time()
    elapsed = (end - start) * 1000  # Convert to milliseconds
    
    if isinstance(result, pd.DataFrame):
        output_size = result.shape[1]
    else:
        output_size = 1
    
    return {
        'name': name,
        'time_ms': elapsed,
        'output_size': output_size
    }

# Generate test data
np.random.seed(42)
categories = [f"cat_{i}" for i in range(100)]
data = pd.Series(np.random.choice(categories, size=10000))

print("Encoding Techniques Benchmark")
print("="*60)
print(f"Data size: {len(data)} samples")
print(f"Unique categories: {data.nunique()}")
print("="*60)

results = []

# Frequency encoding
results.append(benchmark_encoding(
    lambda x: frequency_encode(x),
    data,
    "Frequency Encoding"
))

# Label encoding
results.append(benchmark_encoding(
    lambda x: label_encode(x.tolist()),
    data,
    "Label Encoding"
))

# One-hot encoding
df_test = pd.DataFrame({"category": data})
results.append(benchmark_encoding(
    lambda x: one_hot_encode(x, columns=["category"]),
    df_test,
    "One-Hot Encoding"
))

# Binary encoding
results.append(benchmark_encoding(
    lambda x: binary_encode(x),
    data,
    "Binary Encoding"
))

# Print results
print("\nResults:")
print("-"*60)
for result in results:
    print(f"{result['name']:20s} | Time: {result['time_ms']:8.2f} ms | Output size: {result['output_size']}")

