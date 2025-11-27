"""
Tests for Frequency Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from FrequencyEncoding import frequency_encode
import pandas as pd


def test_frequency_encode():
    """Test frequency encoding function"""
    data = pd.Series(["A", "B", "A", "B", "C"])
    encoded = frequency_encode(data)
    
    assert len(encoded) == 5
    assert encoded["A"] == encoded.iloc[2]  # Same values should have same frequency
    print("Frequency encoding test passed!")


if __name__ == "__main__":
    test_frequency_encode()

