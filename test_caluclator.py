import pytest
from calculator import square_root, factorial, natural_log, power

def test_square_root():
    assert square_root(16) == 4
    assert square_root(0) == 0

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_natural_log():
    # Use pytest.approx to handle floating point comparisons
    assert natural_log(1) == pytest.approx(0)
    assert natural_log(2.71828) == pytest.approx(1, abs=1e-5)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 0.5) == 2