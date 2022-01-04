import pytest
from testingonly.mymath import MyCalc  # Import the MyCalc Class


def test_mycalc():
    # Create the MyCalc Class
    calc = MyCalc()

    # Assert that the calculator sums correctly
    assert calc.sum(1, 2) == 3
