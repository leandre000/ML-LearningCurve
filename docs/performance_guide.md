# Performance Guide

## Encoding Performance Comparison

### Speed (Fastest to Slowest)
1. Label Encoding
2. Frequency Encoding
3. Binary Encoding
4. Hash Encoding
5. One-Hot Encoding
6. Target Encoding
7. Leave-One-Out Encoding

### Memory Usage (Lowest to Highest)
1. Label Encoding
2. Frequency Encoding
3. Binary Encoding
4. Hash Encoding
5. Target Encoding
6. One-Hot Encoding

### When to Optimize

- **Large datasets (>1M rows)**: Use frequency, binary, or hash encoding
- **Many categories (>1000)**: Avoid one-hot, use hash or binary
- **Real-time inference**: Prefer label or frequency encoding
- **Memory constraints**: Use binary or hash encoding

## Benchmarking

Use the benchmark script to measure performance on your data:

```bash
python benchmarks/encoding_benchmark.py
```

