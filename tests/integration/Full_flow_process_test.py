# tests/integration/full_flow_test.py
import pytest
from main import process, Result
from Flow.Action import save_action

def test_full_flow_print(monkeypatch):
    # Capture print output from print_action
    printed = []
    monkeypatch.setattr("builtins.print", lambda x: printed.append(x))

    # Run the process function
    result = process(250, 0.15, save=False)

    # Check the returned Result object
    assert isinstance(result, Result)
    assert result.amount == 250
    assert result.tax == 0.15
    assert result.taxes == 37.5
    assert result.total == 287.5

    # Check that print_action was called
    assert str(result) in [str(p) for p in printed]

def test_full_flow_save(tmp_path):
    # Use a temporary file to avoid writing to the real result.txt
    file_path = tmp_path / "output.txt"

    result = process(150, 0.2, save=False)

    # Save manually to temporary file
    save_action(result, path=file_path)
    content = file_path.read_text(encoding="utf-8")

    # Verify the content
    assert "amount=150" in content
    assert "tax=0.2" in content
    assert "taxes=30.0" in content
    assert "total=180.0" in content

def test_full_flow_invalid_amount():
    # Check that negative amount raises ValueError
    with pytest.raises(ValueError) as excinfo:
        process(-50, 0.1, save=False)
    assert "Amount must be greater than 0" in str(excinfo.value)

def test_full_flow_invalid_tax():
    # Check that tax outside 0-1 range raises ValueError
    with pytest.raises(ValueError) as excinfo:
        process(100, 1.5, save=False)
    assert "The taxes must be a number between 0 and 1" in str(excinfo.value)
