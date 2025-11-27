"""
Configuration file for ML Learning Curve project
"""

# Default encoding parameters
DEFAULT_ENCODING_CONFIG = {
    'frequency': {
        'normalize': True
    },
    'one_hot': {
        'drop_first': False,
        'dtype': int
    },
    'binary': {
        'n_bits': None  # Auto-calculate
    },
    'target': {
        'smoothing': 1.0
    },
    'hash': {
        'n_features': 10
    }
}

# Data paths
DATA_DIR = "data"
EXAMPLES_DIR = "examples"
OUTPUT_DIR = "output"

