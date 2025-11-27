"""
Script to run all tests
"""

import os
import sys
import subprocess

tests_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests')

test_files = [
    'test_frequency_encoding.py',
    'test_label_encoding.py',
    'test_one_hot_encoding.py',
    'test_binary_encoding.py',
    'test_target_encoding.py',
    'test_ordinal_encoding.py',
    'test_utils.py'
]

print("Running all tests...\n")
print("="*60)

for test_file in test_files:
    test_path = os.path.join(tests_dir, test_file)
    if os.path.exists(test_path):
        print(f"\nRunning {test_file}...")
        print("-"*60)
        try:
            subprocess.run([sys.executable, test_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Test failed in {test_file}: {e}")
    else:
        print(f"Test file not found: {test_file}")

print("\n" + "="*60)
print("All tests completed!")

