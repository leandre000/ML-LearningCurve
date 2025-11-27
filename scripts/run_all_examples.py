"""
Script to run all encoding examples
"""

import os
import sys
import subprocess

examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'examples')

examples = [
    'frequency_encoding_example.py',
    'label_encoding_example.py',
    'one_hot_encoding_example.py',
    'comparison_example.py',
    'binary_encoding_example.py',
    'target_encoding_example.py'
]

print("Running all encoding examples...\n")
print("="*60)

for example in examples:
    example_path = os.path.join(examples_dir, example)
    if os.path.exists(example_path):
        print(f"\nRunning {example}...")
        print("-"*60)
        try:
            subprocess.run([sys.executable, example_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {example}: {e}")
    else:
        print(f"Example not found: {example}")

print("\n" + "="*60)
print("All examples completed!")

