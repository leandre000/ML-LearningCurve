"""
Tests for One-Hot Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from one_hot_encoding import one_hot_encode
import pandas as pd


def test_one_hot_encode():
    """Test one-hot encoding function"""
    data = {"color": ["red", "green", "blue"]}
    df = pd.DataFrame(data)
    encoded_df = one_hot_encode(df, columns=["color"])
    
    assert "color" not in encoded_df.columns
    assert "color_red" in encoded_df.columns or "color_Red" in encoded_df.columns
    print("One-hot encoding test passed!")


if __name__ == "__main__":
    test_one_hot_encode()

