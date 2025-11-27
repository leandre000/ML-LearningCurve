"""
Tests for Label Encoding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from labelEncoding import label_encode


def test_label_encode():
    """Test label encoding function"""
    data = ["small", "medium", "large"]
    encoded, encoder = label_encode(data)
    
    assert len(encoded) == 3
    assert len(set(encoded)) == 3  # All should be unique
    print("Label encoding test passed!")


if __name__ == "__main__":
    test_label_encode()

