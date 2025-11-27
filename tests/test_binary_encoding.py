"""
Tests for Binary Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.binary_encoding import binary_encode
import pandas as pd


def test_binary_encode():
    """Test binary encoding function"""
    data = pd.Series(["A", "B", "C", "D"])
    encoded_df = binary_encode(data)
    
    assert encoded_df.shape[0] == 4
    assert encoded_df.shape[1] == 2  # 4 categories need 2 bits
    print("Binary encoding test passed!")


if __name__ == "__main__":
    test_binary_encode()

