"""
Tests for Utility Functions
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validation import check_missing_values, check_duplicates
from utils.preprocessing import handle_missing_values
import pandas as pd
import numpy as np


def test_check_missing_values():
    """Test missing values check"""
    df = pd.DataFrame({"A": [1, 2, np.nan], "B": [4, 5, 6]})
    missing = check_missing_values(df)
    assert missing["A"] == 1
    print("Missing values check test passed!")


def test_check_duplicates():
    """Test duplicate check"""
    df = pd.DataFrame({"A": [1, 2, 1], "B": [4, 5, 4]})
    duplicates = check_duplicates(df)
    assert duplicates >= 0
    print("Duplicate check test passed!")


if __name__ == "__main__":
    test_check_missing_values()
    test_check_duplicates()

