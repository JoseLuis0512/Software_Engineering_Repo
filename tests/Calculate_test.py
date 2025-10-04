import pytest 
from Flow import calc_tax, calc_total

def test_calc_tax():
    assert calc_tax(100, 0.1) == 10
    assert calc_tax(200, 0.2) == 40
    assert calc_tax(0, 0.1) == 0

def test_calc_total():
    assert calc_total(100, 0.1) == 110
    assert calc_total(200, 0.2) == 240
    assert calc_total(0, 0.1) == 0