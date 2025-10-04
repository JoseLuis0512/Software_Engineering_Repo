import pytest
from Flow.Validation import validate_amount, validate_taxes

def test_validate_amount():
    ok, msg = validate_amount(100)
    assert ok
    ok, msg = validate_amount(-1)
    assert not ok
    ok, msg = validate_amount("abc")
    assert not ok

def test_validate_taxes():
    ok, msg = validate_taxes(0.1)
    assert ok
    ok, msg = validate_taxes(-0.1)
    assert not ok
    ok, msg = validate_taxes(1.5)
    assert not ok
