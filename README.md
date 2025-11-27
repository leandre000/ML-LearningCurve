# ML Learning Curve

A comprehensive collection of machine learning algorithms and techniques for educational purposes.

## Overview

This repository contains implementations of various machine learning concepts, focusing on data preprocessing techniques and encoding methods.

## Features

### Encoding Techniques
- Frequency Encoding
- Label Encoding
- One-Hot Encoding
- Binary Encoding
- Target Encoding
- Hash Encoding
- Ordinal Encoding
- Mean Encoding

### Utilities
- Data loading (CSV, Excel)
- Data validation
- Missing value handling
- Feature scaling (Standard, Min-Max)
- Encoding comparison tools

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Each encoding technique is implemented as a standalone module with example usage.

### Quick Start

```python
from FrequencyEncoding import frequency_encode
import pandas as pd

data = {"color": ["red", "green", "blue", "red"]}
df = pd.DataFrame(data)
df['color_freq'] = frequency_encode(df['color'])
```

### Running Examples

```bash
python scripts/run_all_examples.py
```

### Running Tests

```bash
python scripts/run_tests.py
```

## Project Structure

```
ml-1/
├── encoding/          # Encoding technique implementations
├── examples/          # Usage examples
├── tests/             # Unit tests
├── utils/             # Utility functions
├── notebooks/         # Jupyter notebooks
└── scripts/           # Helper scripts
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

