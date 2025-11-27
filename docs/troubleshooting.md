# Troubleshooting Guide

## Common Issues

### Import Errors

If you encounter import errors, make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### Memory Issues with One-Hot Encoding

One-hot encoding can create very large DataFrames. Consider using:
- Binary encoding for high cardinality features
- Hash encoding for very high cardinality
- Frequency encoding as an alternative

### Missing Values

Some encoding techniques may not handle missing values well. Use the preprocessing utilities:

```python
from utils.preprocessing import handle_missing_values
df_clean = handle_missing_values(df, strategy='mode')
```

### Performance Issues

For large datasets:
- Use binary or hash encoding instead of one-hot
- Consider frequency encoding for memory efficiency
- Use the benchmark script to compare performance

