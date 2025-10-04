# tests/integration/Process_test.py
import pytest
from main import process, Result
from Flow.Action import save_action

def test_full_flow(monkeypatch):
    # Capture print output
    printed = []
    monkeypatch.setattr("builtins.print", lambda x: printed.append(x))

    result = process(200, 0.1, save=False)

    # Check result type and values
    assert isinstance(result, Result)
    assert result.amount == 200
    assert result.tax == 0.1
    assert result.taxes == 20
    assert result.total == 220

    # Check print_action executed
    assert str(result) in [str(p) for p in printed]

def test_save_action(tmp_path):
    file_path = tmp_path / "output.txt"
    result = process(100, 0.2, save=False)

    # Save manually in temp file
    save_action(result, path=file_path)
    content = file_path.read_text(encoding="utf-8")

    assert "amount=100" in content
    assert "total=120" in content

def test_invalid_amount():
    with pytest.raises(ValueError) as excinfo:
        process(-10, 0.1, save=False)
    # Updated to match main.py error message
    assert "Amount must be greater than 0" in str(excinfo.value)

def test_invalid_tax():
    with pytest.raises(ValueError) as excinfo:
        process(100, 2.0, save=False)
    # Updated to match main.py error message
    assert "The taxes must be a number between 0 and 1" in str(excinfo.value)
