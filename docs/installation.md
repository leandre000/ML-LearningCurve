# Installation Guide

## Requirements

- Python 3.8 or higher
- pip package manager

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/leandre000/ML-LearningCurve.git
cd ML-LearningCurve
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Verify installation:
```bash
python -c "import pandas; import sklearn; print('Installation successful!')"
```

## Development Installation

For development, install in editable mode:

```bash
pip install -e .
```

## Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

