# Quick Start Guide

Get started with ML Learning Curve in 5 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/leandre000/ML-LearningCurve.git
cd ML-LearningCurve

# Install dependencies
pip install -r requirements.txt

# Validate installation
python scripts/validate_installation.py
```

## Basic Usage

### 1. Frequency Encoding

```python
from FrequencyEncoding import frequency_encode
import pandas as pd

data = {"color": ["red", "green", "blue", "red", "green"]}
df = pd.DataFrame(data)
df['color_freq'] = frequency_encode(df['color'])
print(df)
```

### 2. Label Encoding

```python
from labelEncoding import label_encode

data = ["small", "medium", "large", "small"]
encoded = label_encode(data)
print(encoded)
```

### 3. One-Hot Encoding

```python
from one_hot_encoding import one_hot_encode
import pandas as pd

data = {"category": ["A", "B", "C"]}
df = pd.DataFrame(data)
encoded_df = one_hot_encode(df, columns=["category"])
print(encoded_df)
```

### 4. Automatic Encoding Selection

```python
from utils.encoding_selector import get_encoding_recommendations
import pandas as pd

df = pd.DataFrame({"category": ["A", "B", "C", "A", "B"]})
recommendations = get_encoding_recommendations(df)
print(recommendations)
```

## Next Steps

- Check out the [examples](examples/) directory for more use cases
- Read the [encoding guide](docs/encoding_guide.md) for detailed information
- Run benchmarks: `python benchmarks/encoding_benchmark.py`

