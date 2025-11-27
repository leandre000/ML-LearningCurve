"""
Tests for Weight of Evidence Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.woe_encoding import woe_encode
import pandas as pd


def test_woe_encode():
    """Test WoE encoding function"""
    series = pd.Series(["A", "B", "A", "B"])
    target = pd.Series([1, 0, 1, 0])
    encoded = woe_encode(series, target)
    
    assert len(encoded) == 4
    print("WoE encoding test passed!")


if __name__ == "__main__":
    test_woe_encode()

