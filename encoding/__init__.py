"""
Encoding Techniques Package

A comprehensive collection of categorical encoding techniques for machine learning.
"""

from FrequencyEncoding import frequency_encode
from labelEncoding import label_encode
from one_hot_encoding import one_hot_encode
from encoding.binary_encoding import binary_encode
from encoding.target_encoding import target_encode
from encoding.hash_encoding import hash_encode
from encoding.ordinal_encoding import ordinal_encode
from encoding.mean_encoding import mean_encode
from encoding.woe_encoding import woe_encode
from encoding.leave_one_out_encoding import leave_one_out_encode
from encoding.backward_difference_encoding import backward_difference_encode
from encoding.helmert_encoding import helmert_encode

__version__ = "1.0.0"

__all__ = [
    'frequency_encode',
    'label_encode',
    'one_hot_encode',
    'binary_encode',
    'target_encode',
    'hash_encode',
    'ordinal_encode',
    'mean_encode',
    'woe_encode',
    'leave_one_out_encode',
    'backward_difference_encode',
    'helmert_encode'
]
