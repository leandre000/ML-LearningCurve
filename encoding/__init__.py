"""
Encoding Techniques Package
"""

from FrequencyEncoding import frequency_encode
from labelEncoding import label_encode
from one_hot_encoding import one_hot_encode
from encoding.binary_encoding import binary_encode
from encoding.target_encoding import target_encode
from encoding.hash_encoding import hash_encode
from encoding.ordinal_encoding import ordinal_encode
from encoding.mean_encoding import mean_encode

__all__ = [
    'frequency_encode',
    'label_encode',
    'one_hot_encode',
    'binary_encode',
    'target_encode',
    'hash_encode',
    'ordinal_encode',
    'mean_encode'
]
