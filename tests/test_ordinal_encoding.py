"""
Tests for Ordinal Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.ordinal_encoding import ordinal_encode
import pandas as pd


def test_ordinal_encode():
    """Test ordinal encoding function"""
    data = pd.Series(["small", "medium", "large"])
    encoded = ordinal_encode(data, categories=["small", "medium", "large"])
    
    assert encoded.iloc[0] == 0
    assert encoded.iloc[1] == 1
    assert encoded.iloc[2] == 2
    print("Ordinal encoding test passed!")


if __name__ == "__main__":
    test_ordinal_encode()

