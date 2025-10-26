import os
from Flow.Action import Result, save_action, print_action

def test_result_dataclass():
    r = Result(101, 0.1, 10, 110)
    assert r.amount == 101
    assert r.tax == 0.1
    assert r.taxes == 10
    assert r.total == 110

def test_save_action(tmp_path):
    r = Result(100, 0.1, 10, 110)
    file = tmp_path / "test.txt"
    save_action(r, path=file)
    content = file.read_text()
    assert "Result(amount=100" in content
