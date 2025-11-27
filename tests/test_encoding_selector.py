"""
Tests for Encoding Selector
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.encoding_selector import select_encoding, get_encoding_recommendations
import pandas as pd


def test_select_encoding_low_cardinality():
    """Test encoding selection for low cardinality"""
    data = pd.Series(["A", "B", "C"])
    encoding = select_encoding(data)
    assert encoding in ["one_hot", "binary"]
    print("Low cardinality encoding selection test passed!")


def test_select_encoding_ordinal():
    """Test encoding selection for ordinal data"""
    data = pd.Series(["small", "medium", "large"])
    encoding = select_encoding(data, is_ordinal=True)
    assert encoding in ["ordinal", "label"]
    print("Ordinal encoding selection test passed!")


def test_get_encoding_recommendations():
    """Test encoding recommendations"""
    data = {
        "cat1": ["A", "B", "C"],
        "cat2": [f"X{i}" for i in range(150)]
    }
    df = pd.DataFrame(data)
    recommendations = get_encoding_recommendations(df)
    
    assert "cat1" in recommendations
    assert "cat2" in recommendations
    print("Encoding recommendations test passed!")


if __name__ == "__main__":
    test_select_encoding_low_cardinality()
    test_select_encoding_ordinal()
    test_get_encoding_recommendations()

