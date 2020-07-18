from bandpassfilter import BandPass
import pytest

# @pytest.fixture
# def bandpass():
#     bp = BandPass()
#     return bp

def test_returns_same_arr_within_limits():
    bp = BandPass(10, 20, [10, 20])
    assert bp.filter() == [10,20]

def test_returns_below_min_val_raised_to_min():
    bp = BandPass(10, 20, [9, 20])
    assert bp.filter() == [10, 20]

def test_returns_above_max_val_lowered_to_max():
    bp = BandPass(10, 20, [10, 21])
    assert bp.filter() == [10, 20]

def test_is_integer():
    bp = BandPass(10, 20, [10, 21])
    assert bp.validator() == [10, 21]

def test_is_integer_3():
    bp = BandPass(9, 20, [9, 15, 20])
    assert bp.validator() == [9, 15, 20]

def test_is_not_integer():
    bp = BandPass(9, 20, ["f", 21])
    with pytest.raises(ValueError):
        bp.validator()