def test_environment_baseline():
    """Verify that pytest configuration and basic math run successfully."""
    assert 1 + 1 == 2

def test_imports():
    """Ensure our primary processing packages are present in the runner environment."""
    import pandas as pd
    import numpy as np
    import sklearn
    assert pd.__version__ is not None