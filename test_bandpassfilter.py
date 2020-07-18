from bandpassfilter import *
import pytest

def test_returns_same_arr_within_limits():
    assert bandpass(10,20, [10, 20]) == [10,20]

def test_returns_below_min_val_raised_to_min():
    assert bandpass(10, 20, [9, 20]) == [10, 20]

def test_returns_above_max_val_lowered_to_max():
    assert bandpass(10, 20, [10, 21]) == [10,20]