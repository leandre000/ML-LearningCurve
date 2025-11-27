"""
Tests for Target Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.target_encoding import target_encode
import pandas as pd


def test_target_encode():
    """Test target encoding function"""
    series = pd.Series(["A", "B", "A", "B"])
    target = pd.Series([1, 0, 1, 0])
    encoded = target_encode(series, target)
    
    assert len(encoded) == 4
    print("Target encoding test passed!")


if __name__ == "__main__":
    test_target_encode()

