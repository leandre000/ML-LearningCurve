"""
Tests for Leave-One-Out Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from encoding.leave_one_out_encoding import leave_one_out_encode
import pandas as pd


def test_leave_one_out_encode():
    """Test leave-one-out encoding function"""
    series = pd.Series(["A", "B", "A", "B"])
    target = pd.Series([10, 20, 15, 25])
    encoded = leave_one_out_encode(series, target)
    
    assert len(encoded) == 4
    print("Leave-one-out encoding test passed!")


if __name__ == "__main__":
    test_leave_one_out_encode()

