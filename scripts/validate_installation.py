"""
Script to validate installation and dependencies
"""

import sys

def check_imports():
    """Check if all required packages can be imported"""
    required_packages = [
        'pandas',
        'numpy',
        'sklearn',
        'matplotlib',
        'seaborn'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'sklearn':
                __import__('sklearn')
            else:
                __import__(package)
            print(f"✓ {package} imported successfully")
        except ImportError:
            print(f"✗ {package} not found")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install -r requirements.txt")
        return False
    else:
        print("\n✓ All required packages are installed!")
        return True


def check_modules():
    """Check if project modules can be imported"""
    try:
        from FrequencyEncoding import frequency_encode
        from labelEncoding import label_encode
        from one_hot_encoding import one_hot_encode
        print("✓ Core encoding modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Error importing modules: {e}")
        return False


if __name__ == "__main__":
    print("Validating ML Learning Curve Installation")
    print("="*50)
    
    print("\nChecking required packages...")
    packages_ok = check_imports()
    
    print("\nChecking project modules...")
    modules_ok = check_modules()
    
    print("\n" + "="*50)
    if packages_ok and modules_ok:
        print("✓ Installation validation successful!")
        sys.exit(0)
    else:
        print("✗ Installation validation failed!")
        sys.exit(1)

