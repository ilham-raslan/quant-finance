import math
import pytest
from quantfin.bootstrap.interpolation import LogLinearInterpolator

def test_loglinear_interpolator():
    interpolator = LogLinearInterpolator([1, 2], [1, 2])
    assert interpolator(1.5) == pytest.approx(math.sqrt(2))
