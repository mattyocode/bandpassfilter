from bandpassfilter import BandPass
import pytest

# @pytest.fixture
# def create_bandpass():
#     bp = BandPass()
#     return bp

bp = BandPass()

def test_returns_same_arr_within_limits():
    assert bp.bandpass(10,20, [10, 20]) == [10,20]

def test_returns_below_min_val_raised_to_min():
    assert bp.bandpass(10, 20, [9, 20]) == [10, 20]

def test_returns_above_max_val_lowered_to_max():
    assert bp.bandpass(10, 20, [10, 21]) == [10, 20]

def test_is_integer():
    assert bp.validator([10, 21]) == [10, 21]

# def test_is_not_integer():
#     assert bp.validator(["f", 21]) == False