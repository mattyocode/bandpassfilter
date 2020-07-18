from bandpassfilter import *
import pytest

def test_returns_same_arr_within_limits():
    output = bandpass(10,20, [10, 20])
    assert output == [10,20]